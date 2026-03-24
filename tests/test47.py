programma_naam = "Werken met Data Dictionaries"

def vul_dictionary_met_jaren(start_jaar, einde_jaar):
    data_dictionary_met_jaren = {}
    year = start_jaar
    while year <= einde_jaar:
        data_dictionary_met_jaren[year] = "Maandcollectie"
        year = year + 1
       
    return data_dictionary_met_jaren

def vul_dictionary_met_maanden(data_dictionary_met_jaren, einde_jaar):
    gevulde_data_dictionary = data_dictionary_met_jaren
    maandset = {1,2,3,4,5,6,7,8,9,10,11,12}
    # Vervang de values ("Maandcollectie") van alle jaren met een set van maandnummers 
    ...
    for year in data_dictionary_met_jaren:
        gevulde_data_dictionary[year] = maandset
    return gevulde_data_dictionary

# Hoofdprogramma
if __name__ == '__main__':
    jaar_maand_dictionary = vul_dictionary_met_jaren(2020, 2026)
    print(jaar_maand_dictionary)
    jaar_maand_dictionary = vul_dictionary_met_maanden(jaar_maand_dictionary, 2026)
    print(jaar_maand_dictionary)