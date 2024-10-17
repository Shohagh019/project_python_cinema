class StarCinema:
    def __init__(self):
        self.__hall_list = []

    def entry_hall(self, hall_ob):
        self.__hall_list.append(hall_ob)

    def get_halls(self):
        return self.__hall_list


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[show_id] = [['0' for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, show_id, seat_positions):
        if show_id not in self.__seats:
            print(f"No show found with ID {show_id}!")
            return

        seat_layout = self.__seats[show_id]
        for row, col in seat_positions:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if seat_layout[row][col] == '0':
                    seat_layout[row][col] = '1'
                    print(f"Seat at row {row}, col {col} booked for show {show_id}!")
                else:
                    print(f"Seat at row {row}, col {col} is already booked!")
            else:
                print(f"Seat at row {row}, col {col} is out of bounds!")

    def view_show_list(self):
        if not self.__show_list:
            print(f"No shows currently running in Hall {self.hall_no}.")
        else:
            print(f"Shows running in Hall {self.hall_no}:")
            for show_id, movie_name, time in self.__show_list:
                print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f"No show found with ID {show_id}.")
            return

        available_seats = [(r, c) for r in range(self.rows) 
                                      for c in range(self.cols) 
                                      if self.__seats[show_id][r][c] == '0']

        if available_seats:
            print(f"Available seats for show {show_id}:")
            for row, col in available_seats:
                print(f"Row {row}, Col {col}")
        else:
            print(f"No available seats for show {show_id}!")

cinema = StarCinema()
hall1 = Hall(5, 5, "A1")
hall2 = Hall(6, 6, "B1")
hall3 = Hall(4, 4, "C1")

cinema.entry_hall(hall1)
cinema.entry_hall(hall2)
cinema.entry_hall(hall3)

hall1.entry_show("S1", "Inception", "12:00 PM")
hall1.entry_show("S2", "The Matrix", "3:00 PM")

hall2.entry_show("S3", "Avatar", "1:00 PM")
hall2.entry_show("S4", "Titanic", "4:00 PM")

hall3.entry_show("S5", "The Dark Knight", "2:00 PM")
hall3.entry_show("S6", "Interstellar", "5:00 PM")


def main():
    while True:
        print("\nOptions:")
        print("1. VIEW ALL SHOWS TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKETS")
        print("4. EXIT")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            for hall in cinema.get_halls():
                hall.view_show_list()

        elif choice == '2':
            hall_no = input("Enter Hall No: ")
            show_id = input("Enter Show ID: ")
            for hall in cinema.get_halls():
                if hall.hall_no == hall_no:
                    hall.view_available_seats(show_id)
                    break
            else:
                print(f"Hall {hall_no} not found!")

        elif choice == '3':
            hall_no = input("Enter Hall No(A1/B1/C1): ")
            show_id = input("Enter Show ID(S1/S2/S3/S4/S5/S6): ")
            ticket_num = int(input("How many tickets?: "))
            seats_to_book = []

            for _ in range(ticket_num):
                row = int(input("Enter Row: "))
                col = int(input("Enter Col: "))
                seats_to_book.append((row, col))

            for hall in cinema.get_halls():
                if hall.hall_no == hall_no:
                    hall.book_seats(show_id, seats_to_book)
                    break
            else:
                print(f"Hall {hall_no} not found!")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

main()
