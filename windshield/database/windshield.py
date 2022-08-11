from dataclasses import dataclass
import sqlite3
import logging


logger = logging.getLogger("windshield")


@dataclass
class WindshieldData:
    brand: str
    model: str
    year: int
    sensor: bool
    camera: bool
    heat: bool
    eurocode: str


def create_windshield(data: WindshieldData, connection: sqlite3.Connection) -> None:
    """adauga in baza de date un windshield nou"""
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO windshields (brand, model, year, sensor, camera, heat, eurocode) 
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, (data.brand, data.model, data.year, data.sensor, data.camera, data.heat, data.eurocode,))
    connection.commit()
      
