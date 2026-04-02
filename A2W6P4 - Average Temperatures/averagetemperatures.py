def calculate_results(temperatures_data):
    temps_1995 = [float(x) for x in temperatures_data[0][2]]
    temps_2010 = [float(x) for x in temperatures_data[1][2]]
    temps_2020 = [float(x) for x in temperatures_data[2][2]]
    common_95_10 = len(set(temps_1995) & set(temps_2010))
    common_95_20 = len(set(temps_1995) & set(temps_2020))
    years = [year[0] for year in temperatures_data]
    max_temps_per_year = [max(temps_1995), max(temps_2010), max(temps_2020)]
    highest_temp_year = years[max_temps_per_year.index(max(max_temps_per_year))]
    avg_temps = [
        sum(temps_1995) / len(temps_1995),
        sum(temps_2010) / len(temps_2010),
        sum(temps_2020) / len(temps_2020)
    ]
    warmest_march_year = years[avg_temps.index(max(avg_temps))]
    print(f"{common_95_10:02d}")
    print(f"{common_95_20:02d}")
    print(highest_temp_year)
    print(warmest_march_year)


if __name__ == "__main__":
    MARCH_1995 = [
        '47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6',
        '43.2', '46.2', '45.8', '44.9', '39.4', '40.5', '42.0', '46.5', '46.2',
        '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8',
        '35.2', '38.5', '40.5', '47.0'
    ]
    MARCH_2010 = [
        '39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3',
        '33.3', '37.3', '39.9', '40.8', '42.9', '42.7', '42.6', '44.8', '50.3',
        '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6',
        '46.2', '49.6', '50.1', '43.6'
    ]
    MARCH_2020 = [
        '43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6',
        '50.5', '51.5', '47.7', '44.7', '44.0', '48.9', '45.3', '46.6', '49.7',
        '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4',
        '45.5', '40.7', '39.5', '40.6'
    ]

    TEMPERATURE_DATASET = (
        ('1995', '3', MARCH_1995),
        ('2010', '3', MARCH_2010),
        ('2020', '3', MARCH_2020)
    )

    calculate_results(TEMPERATURE_DATASET)