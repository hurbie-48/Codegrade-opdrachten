import re
licenseplate = input("License: ").strip()
def isLicenceplateValid(licenceplate:str) -> str:
    patterns = [
        r"^[A-Z]{2}-\d{2}-\d{2}$", 
        r"^\d{2}-\d{2}-[A-Z]{2}$",  
        r"^\d{2}-[A-Z]{2}-\d{2}$",  
        r"^[A-Z]{2}-\d{2}-[A-Z]{2}$",   
        r"^[A-Z]{2}-[A-Z]{2}-\d{2}$",   
        r"^\d{2}-[A-Z]{2}-[A-Z]{2}$",   
        r"^\d{2}-[A-Z]{3}-\d$",     
        r"^\d-[A-Z]{3}-\d{2}$",    
        r"^[A-Z]{2}-\d{3}-[A-Z]$",   
        r"^[A-Z]-\d{3}-[A-Z]{2}$",   
        r"^[A-Z]{3}-\d{2}-[A-Z]$",   
        r"^\d-[A-Z]{2}-\d{3}$"     
    ]
    master_pattern = "|".join(patterns)
    if re.fullmatch(master_pattern, licenseplate):
        print("Valid")
    else:
        print("Invalid")
isLicenceplateValid(licenseplate)