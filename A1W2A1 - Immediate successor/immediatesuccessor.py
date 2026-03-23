months = {
    "01" : "31",
    "02" : "28",
    "03" : "31",
    "04" : "30",
    "05" : "31",
    "06" : "30",
    "07" : "31",
    "08" : "31",
    "09" : "30",
    "10" : "31",
    "11" : "30",
    "12" : "31"
}

def is_input_valid(inp_date:str) -> bool:
    if "/" in inp_date:
        return False
    elif "_" in inp_date:
        return False
    elif int(splitDatum(inp_date)[2]) > 31:
        return False
    elif int(splitDatum(inp_date)[1]) > 12:
        return False
    else:
        return True

def splitDatum(datum:str) -> list:
    return datum.split("-")

def reconstructDate(dagen:int, maanden:int, jaren:str) -> str:
    dag = dagen
    if dagen < 10:
        dag = f"0{dagen}"
    maand = maanden
    if maanden < 10:
        maand = f"0{maanden}"
    
    return(f"Next Date: {jaren}-{maand}-{dag}")

datum = input()
if is_input_valid(datum) == True:
    jaren = splitDatum(datum)[0]
    dagen = splitDatum(datum)[2]
    maanden = splitDatum(datum)[1]

    if dagen == months[str(maanden)]:
        jaren = int(jaren)
        maanden = int(maanden)
        maanden += 1
        dagen = "01"
        if maanden > 12:
            maanden = "01"
            jaren += 1
    else:
        dagen = int(dagen)
        dagen += 1

    datum = reconstructDate(int(dagen), int(maanden), str(jaren))
    print(datum)
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")