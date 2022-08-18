from dataclasses import dataclass
import sqlite3
import logging


logger = logging.getLogger("windshield")

@dataclass
class Windshield:
    id: int
    brand: str
    model: str
    start_year: int
    end_year: int | None
    sensor: bool
    camera: bool
    heat: bool
    eurocode: str  
@dataclass
class WindshieldCreateData:
    brand: str
    model: str
    start_year: int
    end_year: int | None
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
            INSERT INTO windshields (brand, model, start_year, end_year, sensor, camera, heat, eurocode) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (data.brand, data.model, data.start_year, data.end_year, data.sensor, data.camera, data.heat, data.eurocode,))
            self._connection.commit()
        except sqlite3.IntegrityError:
            raise EurocodeExists()     
        logger.info("Windshield inserted into database.")

    def search_eurocode(self, data: WindshieldSearchData) -> str | None:
        cursor = self._connection.cursor()
        result = cursor.execute("""SELECT eurocode FROM windshields 
        WHERE brand = ? collate nocase and model = ? collate nocase and start_year <= ? and (end_year is NULL or end_year  >= ?) and sensor = ? 
        and camera = ? and heat = ?;
        """, (data.brand, data.model, data.year, data.year, data.sensor, data.camera, data.heat,))
        row = result.fetchone()
        if row is None:
            return None
        return row[0]    

    def search_windshield(self, eurocode: str) -> Windshield | None: 
        cursor = self._connection.cursor()
        result = cursor.execute("""
        SELECT id, brand, model, start_year, end_year, sensor, camera, heat, eurocode FROM windshields 
        WHERE eurocode = ?;""", (eurocode,))
        row = result.fetchone()
        if row is None:
            return None
        return Windshield(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7], row[8]) 

        
     
        

        
        








        
