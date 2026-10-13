import csv

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_details(self):
        pass


class Student(Person):
    def __init__(self, name, roll_no, marks):
        super().__init__(name)
        self.roll_no=roll_no
        self.marks=marks

    #calculate average marks
    def calculate_avg_marks(self):
        if len(self.marks) == 0:
            return None

        avg = sum(self.marks) / len(self.marks)
        return avg


    def display_details(self):
        print(f"Student's name: {self.name}")
        print(f"Student's roll number: {self.roll_no}")
        print(f"Student's marks: {self.marks}")

        average = self.calculate_avg_marks()
        if average is not None:
            print(f"Average marks: {average}")



class StudentManagement:
    def __init__(self):
        self.students = []

    #add student
    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    #display students
    def display_students(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        for student in self.students:
            student.display_details()
            print("-" * 30)

    #search student
    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display_details()
                return

        print("Student not found.")

    #update student records
    def update_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                new_name = input("Enter new name: ").strip()
                new_marks = input(
                    "Enter new marks separated by commas: "
                )

                student.name = new_name
                student.marks = [
                    int(mark.strip()) for mark in new_marks.split(",")
                ]

                print("Student record updated successfully!")
                return

        print("Student not found.")

   #delete student records
    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student record deleted successfully!")
                return

        print("Student not found.")

    
    # Save student records to a CSV file
    def save_to_csv(self):
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Roll No", "Name", "Marks"])

            for student in self.students:
                writer.writerow([
                    student.roll_no,
                    student.name,
                    ",".join(map(str, student.marks))
                ])

        print("Student records saved successfully!")


    def load_from_csv(self):
        try:
            with open("students.csv", "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row

                for row in reader:
                    roll_no = int(row[0])
                    name = row[1]
                    marks = [int(mark) for mark in row[2].split(",")]

                    student = Student(name, roll_no, marks)
                    self.students.append(student)

            print("Student records loaded successfully!")

        except FileNotFoundError:
            print("CSV file not found. Starting with an empty student list.")



management = StudentManagement()
management.load_from_csv()

    
    
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Records")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    
    
    if choice == "1":
        name = input("Enter student name: ").strip()
        roll_no = int(input("Enter roll number: "))

        if any(student.roll_no == roll_no for student in management.students):
            print("Error: This roll number already exists.")
        else:
            marks_input = input("Enter marks separated by commas: ")
            marks = [
                int(mark.strip()) for mark in marks_input.split(",")
            ]

            student = Student(name, roll_no, marks)
            management.add_student(student)


    elif choice == "2":
        management.display_students()


    elif choice == "3":
        roll_no = int(input("Enter roll number to search: "))
        management.search_student(roll_no)


    elif choice == "4":
        roll_no = int(input("Enter roll number to update: "))
        management.update_student(roll_no)


    elif choice == "5":
        roll_no = int(input("Enter roll number to delete: "))
        management.delete_student(roll_no)

    elif choice == "6":
        management.save_to_csv()

    elif choice == "7":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")

    
