from cinema import Hall

def main():
    hall1 = Hall(24, 48, 1) 
    hall1.entry_show("1", "Oppenheimer", "10:00")
    hall1.entry_show("2", "Dune: Part Two", "13:00")
    hall1.entry_show("3", "Godzilla x Kong: The New Empire", "16:30")
    hall1.entry_show("4", "No Time To Die", "19:00")

    while True:
        print("\nMenu:")
        print("1. View all shows")
        print("2. View available seats for a show")
        print("3. Book tickets for a show")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hall1.view_show_list()
        elif choice == "2":
            show_id = input("Enter the ID of the show: ")
            hall1.view_available_seats(show_id)
        elif choice == "3":
            show_id = input("Enter the ID of the show: ")
            num_seats = input("Enter the number of seats to book: ")
            seats_to_book = []
            for _ in range(int(num_seats)):
                seat = input("Enter seat (row-col) to book: ")
                row, col = map(int, seat.split('-'))
                seats_to_book.append((row, col))
            hall1.book_seats(show_id, seats_to_book)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()
