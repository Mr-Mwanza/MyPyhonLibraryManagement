class Library:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.seats = {}

    def allocate_seat(self, student_id):
        if self.available_seats > 0:
            seat_number = self.total_seats - self.available_seats + 1
            self.seats[student_id] = seat_number
            self.available_seats -= 1
            print(f"Seat allocated to student {student_id}. Seat Number: {seat_number}")
        else:
            print("No available seats.")

    def deallocate_seat(self, student_id):
        if student_id in self.seats:
            seat_number = self.seats[student_id]
            del self.seats[student_id]
            self.available_seats += 1
            print(f"Seat deallocated for student {student_id}. Seat Number: {seat_number}")
        else:
            print(f"No seat allocated for student {student_id}.")

    def get_allocated_seats(self):
        return self.seats

    def get_student_by_seat(self, seat_number):
        for student_id, allocated_seat in self.seats.items():
            if allocated_seat == seat_number:
                return student_id
        return None


def main():
    total_seats = int(input("Enter Total Number of Seats: "))
    library = Library(total_seats)

    while True:
        print("\n1. Allocate Seat")
        print("2. Deallocate Seat")
        print("3. Get Occupying Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            library.allocate_seat(student_id)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            library.deallocate_seat(student_id)
        elif choice == "3":
            seat_number = int(input("Enter seat number: "))
            student_id = library.get_student_by_seat(seat_number)
            if student_id:
                print(f"Student occupying seat {seat_number}: {student_id}")
            else:
                print(f"No student occupying seat {seat_number}.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
