import pandas as pd

def perform_book_operations():
    try:
        df = pd.read_csv('books.csv')
    except file_not_found_error:
        print('books.csv not found.')
        return
    print('\n--- a) Complete Report of Books ---')
    print(df.to_string(index=False))
    author = 'George Orwell'
    print(f'\n--- b) Books of Author: {author} ---')
    author_books = df[df['name of author'] == author]
    print(author_books.to_string(index=False))
    publisher = 'Scribner'
    print(f'\n--- c) Books of Publisher: {publisher} ---')
    publisher_books = df[df['publishing house'] == publisher]
    print(publisher_books.to_string(index=False))
    cheapest = df.loc[df['price'].idxmin(), 'title']
    costliest = df.loc[df['price'].idxmax(), 'title']
    print(f'\n--- d) Cheapest and Costliest Books ---')
    print(f"Cheapest: {cheapest} (Price: {df['price'].min()})")
    print(f"Costliest: {costliest} (Price: {df['price'].max()})")
    print('\n--- e) Books Sorted by Publication Year ---')
    sorted_df = df.sort_values(by='publication year')
    print(sorted_df.to_string(index=False))
if __name__ == '__main__':
    perform_book_operations()