import sys
import csv
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.file_path = r"C:\Code_Files\Group project\Library Management\library_management.csv"
        self.fine_per_day = 10  # Fine amount per day
        self.load_inventory()

    def load_inventory(self):
        """Load book inventory from CSV file."""
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['Available'] = row['Available'] == 'True'
                    row['Due Date'] = datetime.strptime(row['Due Date'], '%Y-%m-%d') if row['Due Date'] != 'None' else None
                    row['Borrow Count'] = int(row['Borrow Count'])
        except FileNotFoundError:
            print("No previous inventory found. Starting fresh.")

    def save_inventory(self, books):
        """Save book inventory to CSV file."""
        with open(self.file_path, mode='w', newline='') as file:
            fieldnames = ['Title', 'Author', 'ISBN', 'Available', 'Due Date', 'Borrow Count']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in books:
                writer.writerow({
                    'Title': book['Title'],
                    'Author': book['Author'],
                    'ISBN': book['ISBN'],
                    'Available': book['Available'],
                    'Due Date': book['Due Date'].strftime('%Y-%m-%d') if book['Due Date'] else 'None',
                    'Borrow Count': book['Borrow Count']
                })

    def add_book(self, title, author, isbn):
        books = self.read_csv()
        books.append({'Title': title, 'Author': author, 'ISBN': isbn, 'Available': True, 'Due Date': None, 'Borrow Count': 0})
        self.save_inventory(books)
        print(f"Added: {title}")

    def issue_book(self, isbn, borrower):
        books = self.read_csv()
        for book in books:
            if book['ISBN'] == isbn and book['Available']:
                book['Available'] = False
                book['Due Date'] = datetime.now() + timedelta(days=14)
                book['Borrow Count'] += 1
                self.save_inventory(books)
                print(f"Issued: {book['Title']} to {borrower}. Due date: {book['Due Date'].strftime('%Y-%m-%d')}")
                return
        print("Book unavailable or incorrect ISBN")

    def return_book(self, isbn):
        books = self.read_csv()
        for book in books:
            if book['ISBN'] == isbn and not book['Available']:
                overdue_days = max((datetime.now() - book['Due Date']).days, 0)
                fine = overdue_days * self.fine_per_day if overdue_days else 0
                book['Available'] = True
                book['Due Date'] = None
                self.save_inventory(books)
                print(f"Returned: {book['Title']}. Late fine: ₹{fine}" if fine else f"Returned: {book['Title']}")
                return
        print("Invalid return request")

    def list_books(self):
        books = self.read_csv()
        print("\nAvailable Inventory:")
        for book in books:
            status = "Available" if book['Available'] else f"Issued (Due: {book['Due Date']})"
            print(f"{book['Title']} by {book['Author']} (ISBN: {book['ISBN']}) - {status}, Borrowed {book['Borrow Count']} times")

    def read_csv(self):
        try:
            with open(self.file_path, mode='r') as file:
                return [row for row in csv.DictReader(file)]
        except FileNotFoundError:
            return []

def main():
    library = Library()
    while True:
        print("\nLibrary Management System:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. List Books")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            library.add_book(input("Enter title: "), input("Enter author: "), input("Enter ISBN: "))
        elif choice == "2":
            library.issue_book(input("Enter ISBN: "), input("Enter borrower name: "))
        elif choice == "3":
            library.return_book(input("Enter ISBN: "))
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            print("Exiting system...")
            sys.exit()
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()