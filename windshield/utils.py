# functie care transforma din str '.00/01-05/09' intr-un start_year si end_year:
# '.15/01-'

def parse_str_to_years(value: str) -> tuple[int, int]:
    str_start_year = value[1:2]
    if len(value) == 12:
        str_end_year = value[7:8]

