programma_naam = "Werken met Data Dictionaries"

def vul_dictionary_met_jaren(start_jaar, einde_jaar):
    data_dictionary_met_jaren = {}
    # Vul data dictionary met de jaren start_jaar t/m einde_jaar als key
    # En "Maandcollectie" als value
    ...
    for jaar in range(start_jaar,einde_jaar+1):
        data_dictionary_met_jaren[jaar] = "Maandcollectie"
    return data_dictionary_met_jaren

# Hoofdprogramma
if __name__ == '__main__':
    dictionary1 = vul_dictionary_met_jaren(2020, 2026)
    print(dictionary1)
