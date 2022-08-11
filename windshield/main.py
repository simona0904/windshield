import argparse
import sys
import sqlite3
import pathlib
import logging
from windshield.database.windshield import WindshieldData, create_windshield


logger = logging.getLogger("windshield")
cli_handler = logging.StreamHandler()
cli_handler.setLevel(logging.INFO)
logger.addHandler(cli_handler)



ROOT = pathlib.Path(__file__).parent.parent
DB_FILE = ROOT.joinpath("windshield.db")


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command",required=True)
    create_parser = subparsers.add_parser("create-windshield")
    create_parser.add_argument("--brand", required=True)
    create_parser.add_argument("--model", required=True)
    create_parser.add_argument("--year", required=True, type=int, help="an intre 1960 si anul curent")
    create_parser.add_argument("--sensor", action="store_true")
    create_parser.add_argument("--camera", action="store_true")
    create_parser.add_argument("--heat", action="store_true")
    create_parser.add_argument("--eurocode", required=True)
    return parser.parse_args(sys.argv[1:])


def main(): 
    with sqlite3.connect(DB_FILE) as connection:
        args = parse_arguments()
        if args.command == "create-windshield":
            logger.info("User has selected create windshield command.")
            windshield_data = WindshieldData(args.brand, args.model, args.year, args.sensor, args.camera, args.heat, args.eurocode)    
            create_windshield(windshield_data, connection)


if __name__ == "__main__": 
    main()  