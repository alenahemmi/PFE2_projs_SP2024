# Alena Hemminger - PFE2 - Ex 1: Python I choose you
# CSC 103 Spring 2024
import pandas as pd 
import sys
# Connect all datafiles to python file
# Errors in pokemon file were handled manually on excel
encounters = pd.read_csv("/Users/alenahemminger/Library/CloudStorage/OneDrive-CarlowUniversity/Spring24/CSC-103/ex1_pokemon/encounters.csv")
locations = pd.read_csv("/Users/alenahemminger/Library/CloudStorage/OneDrive-CarlowUniversity/Spring24/CSC-103/ex1_pokemon/locations.csv")
pokemon = pd.read_csv("/Users/alenahemminger/Library/CloudStorage/OneDrive-CarlowUniversity/Spring24/CSC-103/ex1_pokemon/pokemon.csv")
regions = pd.read_csv("/Users/alenahemminger/Library/CloudStorage/OneDrive-CarlowUniversity/Spring24/CSC-103/ex1_pokemon/regions.csv")


print("Welcome to your personal Pokédex! This is full of all of the Pokémon since its creation in 1995!")

# create while loop to allow code to run more than once
main_indicator = 1

while main_indicator == 1:
    main_indicator = 0
    print("In your real-life pokedex you can choose to search by one of the following: Pokémon or Region")
    
    
    # indicator to signal loop to make sure input is either 1 or 2
    input_indicator = 1
    while input_indicator == 1:    
        
        # create binary choice for how they search
        entry_choice = input("Please indicate 1 for Pokémon or 2 for Region")
        
        # ----------POKEMON SEARCH-----------
        if entry_choice == '1':
            input_indicator = 0
            print("You chose to search by Pokémon name.")
            pokemon_search = input("Please input the name of the Pokémon you would like to learn more about. (To search variations, simply add a hyphen and the variation name.)")
            # find all info from pokemnon.csv on that pokemon
            # NAME
            print('Name:', pokemon.identifier[pokemon['identifier']==pokemon_search])

            # INDEX NUMBER
            pokemon_identify = pokemon.id[pokemon["identifier"]==pokemon_search]
            print('ID:', pokemon_identify)

            # LOCATIONS FOUND
            pokemon_to_encounters = encounters.location_area_id[encounters['pokemon_id'].isin(pokemon_identify)]
            encounters_to_locations = locations.identifier[locations['id'].isin(pokemon_to_encounters)]
            print(encounters_to_locations)
            
            # LOWEST LEVEL LOCATION
            # find the level
            lowest_encounter_lvl = min(encounters.min_level[encounters['pokemon_id'].isin(pokemon_identify)])
            # find the location
            lowest_location_id = encounters.location_area_id[encounters['min_level'] == lowest_encounter_lvl]
                 # first_lowest_location is made in case there are multiple locations that have that level for that pokemon
            first_lowest_location = int(lowest_location_id.head(1).iloc[0])
            lowest_location_name = locations.identifier[locations['id'] == first_lowest_location]
            print("Lowest level encounter:", lowest_encounter_lvl, "at", lowest_location_name)

            # HIGHEST LEVEL LOCATION
            # find the level
            highest_encounter_lvl = max(encounters.max_level[encounters['pokemon_id'].isin(pokemon_identify)])
            # find the location
            highest_location_id = encounters.location_area_id[encounters['max_level'] == highest_encounter_lvl]
                # first_highest_location
            first_highest_location = int(highest_location_id.head(1).iloc[0])
            highest_location_name = locations.identifier[locations['id'] == first_highest_location]
            print("Highest level encounter:", highest_encounter_lvl, "at", highest_location_name)
            
        # ----------REGION SEARCGH----------
        elif entry_choice == '2':
            input_indicator = 0
            print("You chose to search by region.")
            print(regions)
            region_choice = input("Please choose one of the above regions by their id.")

            linkLocation = locations.region_id[locations['region_id'] == int(region_choice)]
            linkEncounters = encounters.pokemon_id[encounters['location_area_id'].isin(linkLocation)]
            findPokemon = pokemon.identifier[pokemon['id'].isin(linkEncounters)]
            print(findPokemon)

            
            
            
        # loop if input not 1 or 2
        else:
            input_indicator = 1
            print("Invalid input. Try again.")
            
            
            
            
    # choice to restart or to quit
    print("Your real-life Pokédex has provided all of the information it can. Would you like to start a new search or exit?")
    exit_or_restart = input("Please indicate 1 for new search or 2 to exit.")
    if exit_or_restart == '1':
        main_indicator = 1
    elif exit_or_restart == '2':
        main_indicator = 0
    else:
        print("Invalid input, goodbye.")
        main_indicator = 0
sys.exit()
