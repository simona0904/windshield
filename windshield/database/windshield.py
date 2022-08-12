from dataclasses import dataclass
import sqlite3
import logging


logger = logging.getLogger("windshield")


@dataclass
class WindshieldCreateData:
    brand: str
    model: str
    year: int
    sensor: bool
    camera: bool
    heat: bool
    eurocode: str

@dataclass
class WindshieldSearchData:
    brand: str
    model: str
    year: int
    sensor: bool
    camera: bool
    heat: bool
    

class EurocodeExists(Exception):
    pass 


class Database:

    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection    

    def create_windshield(self, data: WindshieldCreateData) -> None:
        """adauga in baza de date un windshield nou"""
        cursor = self._connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO windshields (brand, model, year, sensor, camera, heat, eurocode) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (data.brand, data.model, data.year, data.sensor, data.camera, data.heat, data.eurocode,))
            self._connection.commit()
        except sqlite3.IntegrityError:
            raise EurocodeExists()     
        logger.info("Windshield inserted into database.")

    def search_eurocode(self, data: WindshieldSearchData) -> str | None:
        cursor = self._connection.cursor()
        result = cursor.execute("""SELECT eurocode FROM windshields 
        WHERE brand = ? and model = ? and year = ? and sensor = ? and camera = ? and heat = ?;
        """, (data.brand, data.model, data.year, data.sensor, data.camera, data.heat,))
        row = result.fetchone()
        if row is None:
            return None
        return row[0]    

        
        








        
