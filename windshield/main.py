import argparse
import sys
import sqlite3
import pathlib
import logging
from windshield.database.windshield import Database, EurocodeExists, WindshieldCreateData, WindshieldSearchData


logger = logging.getLogger("windshield")
cli_handler = logging.StreamHandler()
cli_handler.setLevel(logging.INFO)
logger.addHandler(cli_handler)


ROOT = pathlib.Path(__file__).parent.parent
DB_FILE = ROOT.joinpath("windshield.db")


def parse_arguments():
    parser = argparse.ArgumentParser()
    # command este numele variabilei, create-windshield/search-eurocode sunt valorile pt command. 
    subparsers = parser.add_subparsers(dest="command",required=True)
    # se creaza comanda create-winshield:
    create_parser = subparsers.add_parser("create-windshield")
    # se creaza argumentele pt comanda create-windshield.
    create_parser.add_argument("--brand", required=True)
    create_parser.add_argument("--model", required=True, help="modelul autoturismului")
    create_parser.add_argument("--year", required=True, type=int, help="an intre 1960 si anul curent")
    create_parser.add_argument("--sensor", action="store_true")
    create_parser.add_argument("--camera", action="store_true")
    create_parser.add_argument("--heat", action="store_true")
    create_parser.add_argument("--eurocode", required=True)

    # se creaza comanda search-eurocode:
    search_parser = subparsers.add_parser("search-eurocode")
    # se creaza argumentele pt comanda search-eurocode.
    search_parser.add_argument("--brand", required=True)
    search_parser.add_argument("--model", required=True, help="modelul autoturismului")
    search_parser.add_argument("--year", required=True, type=int, help="an intre 1960 si anul curent")
    search_parser.add_argument("--sensor", action="store_true")
    search_parser.add_argument("--camera", action="store_true")
    search_parser.add_argument("--heat", action="store_true")

    return parser.parse_args(sys.argv[1:])


def main(): 
    with sqlite3.connect(DB_FILE) as connection:
        database = Database(connection)
        args = parse_arguments()
        if args.command == "create-windshield":
            logger.info("User has selected create windshield command.")
            windshield_create_data = WindshieldCreateData(args.brand, args.model, args.year, args.sensor, args.camera, args.heat, args.eurocode) 
            try:   
                database.create_windshield(windshield_create_data)
            except EurocodeExists:
                print("Eurocode already exists.")   
            else:
                print("Windshield successfully created.") 
        elif args.command == "search-eurocode":
            windshield_search_data = WindshieldSearchData(args.brand, args.model, args.year, args.sensor, args.camera, args.heat)
            eurocode = database.search_eurocode(windshield_search_data)
            if eurocode is None:
                print("Eurocode not found.")
            else:    
                print(f"Eurocode for windshield is {eurocode}")        


if __name__ == "__main__": 
    main()  