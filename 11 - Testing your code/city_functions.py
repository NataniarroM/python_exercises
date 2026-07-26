def formatted_city_country(city, country, population=""):
    if population:
        formatted = f"{city}, {country} - {population}"
    else:
        formatted = f"{city}, {country}"
    return formatted