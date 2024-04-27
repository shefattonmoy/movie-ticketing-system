class StarCinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall=None):
        if hall:
            cls._hall_list.append(hall)
        else:
            print("No hall provided.")

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

        for row in range(1, rows + 1):
            self._seats[row] = [False] * cols

        StarCinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seats_to_book):
        for row, col in seats_to_book:
            if row in self._seats and 1 <= col <= self._cols:
                if not self._seats[row][col - 1]:
                    self._seats[row][col - 1] = True
                    print(f"Seat {row}-{col} booked successfully for show ID {show_id}.")
                else:
                    print(f"Seat {row}-{col} is already booked.")
            else:
                print(f"Seat {row}-{col} does not exist in the hall.")

    def view_show_list(self):
        if not self._show_list:
            print("No shows are currently running.")
        else:
            print("Shows running in this hall:")
            for show_info in self._show_list:
                print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, show_id):
        for show_info in self._show_list:
            if show_info[0] == show_id:
                available_seats = []
                for row, seats in self._seats.items():
                    for col, booked in enumerate(seats, start=1):
                        if not booked:
                            available_seats.append((row, col))
                if available_seats:
                    print(f"Available seats for show ID {show_id}: {available_seats}")
                else:
                    print(f"No available seats for show ID {show_id}.")
                return
        print(f"No show found with ID {show_id}.")
