import pandas as pd

def diamond_analysis():
    data = {'carat': [0.23, 0.21, 0.23, 0.29, 0.31], 'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'], 'color': ['E', 'E', 'E', 'I', 'J'], 'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'], 'depth': [61.5, 59.8, 56.9, 62.4, 63.3], 'table': [55.0, 61.0, 65.0, 58.0, 58.0], 'price': [326, 326, 327, 334, 335], 'x': [3.95, 3.89, 4.05, 4.2, 4.34], 'y': [3.98, 3.84, 4.07, 4.23, 4.35], 'z': [2.43, 2.31, 2.31, 2.63, 2.75]}
    df = pd.DataFrame(data)
    print('\n--- i) Mean Price for Each Cut ---')
    mean_price = df.groupby('cut')['price'].mean()
    print(mean_price)
    print('\n--- ii) Count, Min, Max Price for Each Cut ---')
    stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
    print(stats)
    print('\n--- iii) Average Value of x, y, and z ---')
    print(f"Average x: {df['x'].mean():.2f}")
    print(f"Average y: {df['y'].mean():.2f}")
    print(f"Average z: {df['z'].mean():.2f}")
if __name__ == '__main__':
    diamond_analysis()