# functie care transforma din str '.00/01-05/09' intr-un start_year si end_year:
# '.15/01-'

def parse_str_to_years(value: str) -> tuple[int, int | None]:
    start_year = int(value[1:3])
    start_year = 2000 + start_year if start_year < 30 else 1900 + start_year
    end_year = None
    if len(value) == 12:
        end_year = int(value[7:9])
        end_year = 2000 + end_year if end_year < 30 else 1900 + end_year
    return (start_year, end_year,)

def parse_str_to_equipment(eurocode: str) ->tuple[bool, bool, bool]:
    sensor = False
    try:
        index_M = eurocode.index("M")
        if eurocode[index_M -1] != "1":
            sensor = True
    except ValueError:
        pass    
    return sensor, False, False