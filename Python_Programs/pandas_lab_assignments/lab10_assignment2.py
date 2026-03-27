import pandas as pd

def perform_state_operations():
    data = {'State': ['Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'Goa', 'Sikkim'], 'Area': [307713, 342239, 240928, 3702, 7096], 'Population': [112374333, 68548437, 199812341, 1458545, 610577]}
    df = pd.DataFrame(data)
    print('\n--- a) Complete Information of States ---')
    print(df.to_string(index=False))
    largest_area_state = df.loc[df['Area'].idxmax(), 'State']
    print(f'\n--- b) State with Largest Area: {largest_area_state} ---')
    largest_population_state = df.loc[df['Population'].idxmax(), 'State']
    print(f'\n--- c) State with Largest Population: {largest_population_state} ---')
    df['Density'] = df['Population'] / df['Area']
    print('\n--- d) Population Density Calculated (Added as new column) ---')
    print(df.to_string(index=False))
    highest_density_state = df.loc[df['Density'].idxmax(), 'State']
    print(f'\n--- e) State with Highest Population Density: {highest_density_state} ---')
if __name__ == '__main__':
    perform_state_operations()