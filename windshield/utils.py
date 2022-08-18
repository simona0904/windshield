# functie care transforma din str '.00/01-05/09' intr-un start_year si end_year:
# '.15/01-'

from typing import Literal

# functie care transforma din str years in start_year si end_year:
def parse_str_to_years(value: str) -> tuple[int, int | None]:
    start_year = int(value[1:3])
    start_year = 2000 + start_year if start_year < 30 else 1900 + start_year
    end_year = None
    if len(value) == 12:
        end_year = int(value[7:9])
        end_year = 2000 + end_year if end_year < 30 else 1900 + end_year
    return (start_year, end_year,)

 # functie care verifica daca exista equipment dupa eurocod:
def equipment_exists(eurocode: str, equipment: Literal["M"] | Literal["C"] | Literal["H"]) -> bool:
    equipment_exists = False
    try:
        index_M = eurocode.index(equipment)       # incercam sa gasim indexul lui M
    except ValueError:                            # daca nu exista M o sa primim value error
        pass                                      # nu facem nimic pt ca by default avem equipment exist false
    else:                                         # daca am agasit M 
        if eurocode[index_M -1] != "1":           # si indexul eurocodului minus 1 != stringul 1
            equipment_exists = True               # atunci avem equipment
    return equipment_exists    

# functie care transforma din str eurocode in echipare sensor, camera, heat
def parse_str_to_equipment(eurocode: str) -> tuple[bool, bool, bool]:
    sensor = equipment_exists(eurocode, "M")
    camera = equipment_exists(eurocode, "C")
    heat = equipment_exists(eurocode, "H")
    return sensor, camera, heat

