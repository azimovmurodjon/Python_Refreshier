###########################################

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in Dictionary

travel_log = {
    "France": {"cities_visited":  ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 10},
}

# Nesting dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
        "total_visits": 10
    },
]

