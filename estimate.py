import pandas as pd
import numpy as np

def calculate_flight_emissions():
    """
    Calculate estimated annual flight emissions for US students studying in Ireland
    """
    # Constants
    TOTAL_STUDENTS = 11700
    
    # 1. Distribution of major US departure regions (estimated based on population centers)
    departure_distribution = {
        'East Coast': 0.45,    # NYC, Boston, DC area
        'Midwest': 0.25,       # Chicago, Detroit
        'West Coast': 0.20,    # LA, SF, Seattle
        'South': 0.10          # Atlanta, Miami
    }
    
    # 2. Representative flight distances to Dublin (km)
    distances = {
        'East Coast': 5500,    # Average NYC-Dublin distance
        'Midwest': 6500,       # Average Chicago-Dublin distance
        'West Coast': 8200,    # Average LA-Dublin distance
        'South': 6800         # Average Atlanta-Dublin distance
    }
    
    # 3. Emissions factors (per passenger per km)
    EMISSIONS_FACTORS = {
        'co2_per_km': 0.115,          # kg CO2 per passenger km
        'contrails_factor': 1.7,      # Additional warming effect from contrails
        'other_ghg_factor': 1.2       # N2O, Ozone formation etc.
    }
    
    # Calculate for each region
    results = []
    for region, percentage in departure_distribution.items():
        num_students = TOTAL_STUDENTS * percentage
        distance = distances[region]
        
        # Round trip emissions (multiply by 2)
        total_distance = distance * 2
        
        # Basic CO2 emissions
        co2_emissions = total_distance * EMISSIONS_FACTORS['co2_per_km'] * num_students
        
        # Total climate impact including contrails and other GHGs
        total_climate_impact = (co2_emissions * 
                              EMISSIONS_FACTORS['contrails_factor'] * 
                              EMISSIONS_FACTORS['other_ghg_factor'])
        
        results.append({
            'Region': region,
            'Number_of_Students': num_students,
            'Total_Distance_km': total_distance,
            'CO2_Emissions_kg': co2_emissions,
            'Total_Climate_Impact_kg_CO2eq': total_climate_impact
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    
    # Calculate totals
    totals = {
        'Total CO2 Emissions (kg)': df['CO2_Emissions_kg'].sum(),
        'Total Climate Impact (kg CO2eq)': df['Total_Climate_Impact_kg_CO2eq'].sum(),
        'Average per Student CO2 (kg)': df['CO2_Emissions_kg'].sum() / TOTAL_STUDENTS,
        'Average per Student Climate Impact (kg CO2eq)': 
            df['Total_Climate_Impact_kg_CO2eq'].sum() / TOTAL_STUDENTS
    }
    
    return df, totals

if __name__ == "__main__":
    # Run calculation
    regional_results, total_results = calculate_flight_emissions()

    for key, value in total_results.items():
        print(key + " : " + str(value))
