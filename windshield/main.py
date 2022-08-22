import argparse
import sys
import sqlite3
from pathlib import Path
import logging
from windshield.logger import configure_logger, LOGGER_NAME
from windshield.commands.request_offer import send_request_offer_email
from .commands.import_excel import import_excel
from windshield.database.windshield import Database, EurocodeExists, WindshieldCreateData, WindshieldSearchData


configure_logger()
logger = logging.getLogger(LOGGER_NAME)

ROOT = Path(__file__).parent.parent
DB_FILE = ROOT.joinpath("windshield.db")


def parse_arguments():
    parser = argparse.ArgumentParser()
    # command este numele variabilei, create-windshield/search-eurocode sunt valorile pt command. 
    subparsers = parser.add_subparsers(dest="command",required=True)
    # se creaza comanda create-winshield:
    create_parser = subparsers.add_parser("create-windshield", 
    help="python -m windshield.main create-windshield --brand ford --model focus --start-year 2002 --sensor --eurocode 3566ags") 
    # se creaza argumentele pt comanda create-windshield.
    create_parser.add_argument("--brand", required=True)
    create_parser.add_argument("--model", required=True)
    create_parser.add_argument("--start-year", required=True, type=int, help="an intre 1960 si anul curent")
    create_parser.add_argument("--end-year", type=int, help="an intre 1960 si anul curent")
    create_parser.add_argument("--sensor", action="store_true")
    create_parser.add_argument("--camera", action="store_true")
    create_parser.add_argument("--heat", action="store_true")
    create_parser.add_argument("--eurocode", required=True)

    # se creaza comanda search-eurocode:
    search_parser = subparsers.add_parser("search-eurocode", 
    help="ex. de utilizare:  python -m windshield.main search-eurocode --brand ford --model focus --year 2014 --sensor --camera --heat")
    # se creaza argumentele pt comanda search-eurocode.
    search_parser.add_argument("--brand", required=True)
    search_parser.add_argument("--model", required=True, help="modelul autoturismului")
    search_parser.add_argument("--year", required=True, type=int, help="an intre 1960 si anul curent")
    search_parser.add_argument("--sensor", action="store_true")
    search_parser.add_argument("--camera", action="store_true")
    search_parser.add_argument("--heat", action="store_true")

    # se creaza comanda request-offer:
    request_offer_parser = subparsers.add_parser("request-offer",
    help="ex. de utilizare: python -m windshield.main request-offer --eurocode 8627AGACMVZ1C --name Andrei --phone 070000000")
    # se creaza argumentele pt comanda request-offer.
    request_offer_parser.add_argument("--eurocode", required=True)
    request_offer_parser.add_argument("--name", required=True)
    request_offer_parser.add_argument("--phone", required=True)

    # se creaza comanda import:
    import_parser = subparsers.add_parser("import")
    import_parser.add_argument("--path")                      # C:\Users\simon\OneDrive\Desktop
    
    # parseaza dintr-un string intr-un obiect args:
    return parser.parse_args(sys.argv[1:])


def main(): 
    with sqlite3.connect(DB_FILE) as connection:
        database = Database(connection)
        logger.info("Connected to database.")
        args = parse_arguments()
        if args.command == "create-windshield":
            logger.info("User has selected create windshield command.")
            windshield_create_data = WindshieldCreateData(args.brand, args.model, args.start_year, args.end_year, args.sensor,
             args.camera, args.heat, args.eurocode) 
            try:   
                database.create_windshield(windshield_create_data)
            except EurocodeExists:
                print("Eurocode already exists.")   
            else:
                print("Windshield successfully created.") 
        elif args.command == "search-eurocode":
            logger.info("User has selected search-eurocode command.")
            windshield_search_data = WindshieldSearchData(args.brand, args.model, args.year, args.sensor, args.camera,
             args.heat)
            eurocode = database.search_eurocode(windshield_search_data)
            if eurocode is None:
                print("Eurocode not found.")
            else:    
                print(f"Eurocode for windshield is {eurocode}") 
        elif args.command == "request-offer":
            logger.info("User has selected request-offer command.")
            windshield = database.search_windshield(args.eurocode) 
            if windshield is None:
                logger.warning("User tried to search eurocode that doesnt exist: %s", args.eurocode)
                print("Eurocode not found")  
            else:
                send_request_offer_email(windshield, args.name, args.phone)
                print("Offer sent.") 
        elif args.command == "import":
            try:
                import_excel(Path(args.path), database)  
            except Exception as e:
                logger.error("Error when importing excel: %s", e)    



if __name__ == "__main__": 
    main()  