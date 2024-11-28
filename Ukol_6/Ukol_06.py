countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",}

countries_name = {}
countries_len = {}

def dict_countries_name():
    for key, value in countries.items():
        countries_name[value] = key
    return countries_name

def countries_value_len():
    for key, value in countries.items():
        countries_len[key] = len(value)
    return countries_len

print(dict_countries_name())
print(countries_value_len())