class Books:
    def __init__(self, author, title, price, publisher, stock):
        self.author = author
        self.title = title
        self.price = price
        self.publisher = publisher
        self.stock = stock

    def display_details(self):
        print(f"\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price}\nPublisher: {self.publisher}\nStock: {self.stock}")

    def check_and_buy(self):
        copies = int(input("Enter number of copies required: "))
        if copies <= self.stock:
            print(f"Total cost: {copies * self.price}")
            self.stock -= copies
        else:
            print("Required number of copies are not available")

def search_books(book_list):
    search_title = input("\nEnter title of the book: ")
    search_author = input("Enter author of the book: ")
    
    for book in book_list:
        if book.title == search_title and book.author == search_author:
            book.display_details()
            book.check_and_buy()
            return
    
    print("Book not available in inventory.")

if __name__ == "__main__":
    inventory = [
        Books("J.K. Rowling", "Harry Potter", 500, "Bloomsbury", 10),
        Books("F. Scott Fitzgerald", "The Great Gatsby", 300, "Scribner", 5),
        Books("George Orwell", "1984", 450, "Secker & Warburg", 20)
    ]
    
    search_books(inventory)
