from dataclasses import dataclass


@dataclass
class Windshield:
    id: int
    brand: str
    model: str
    year: int
    sensor: bool
    camera: bool
    heat: bool
    eurocode: str  