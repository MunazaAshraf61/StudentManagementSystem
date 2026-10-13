# Student Management System (Python OOP Project)

## About the Project

I created this Student Management System using Python as a project to practise my programming skills and understand how object-oriented programming works in a practical application.

The program allows users to manage student records through a simple menu-driven interface. Users can add new students, view their details, search for a student using their roll number, update information, and delete records. It also calculates the average marks of each student and uses a CSV file to store records so they can be loaded again when the program is restarted.

## Features

- **Add Student:** Add a student's name, roll number, and marks.
- **Display Students:** View all saved student records along with their average marks.
- **Search Student:** Find a student using their roll number.
- **Update Student:** Change a student's name and marks.
- **Delete Student:** Remove a student record using the roll number.
- **Save Records:** Save the current student records to a CSV file.
- **Load Records:** Load previously saved records when the program starts.
- **Duplicate Roll Number Check:** Prevent adding a student with a roll number that already exists in the current list.
- **Average Marks Calculation:** Calculate the average of the marks entered for each student.

## Concepts Used

While building this project, I practised the following Python concepts:

- **Object-Oriented Programming (OOP):** Organising the program using classes and objects.
- **Classes and Objects:** Creating and managing student objects.
- **Inheritance:** Using the `Student` class to inherit from the `Person` class.
- **Abstraction:** Using an abstract base class and an abstract method with Python's `abc` module.
- **Lists and Loops:** Storing student objects and processing records.
- **Conditional Statements:** Handling menu choices and searching for matching roll numbers.
- **Functions and Methods:** Separating different operations into reusable methods.
- **CSV File Handling:** Reading student records from a CSV file and saving updated records.
- **Exception Handling:** Handling the situation where the CSV file does not exist.

## Technologies Used

- Python 3
- Python's built-in `csv` module
- Python's built-in `abc` module
- Visual Studio Code

## Project Files

```text
StudentManagementSystem/
│
├── StudentManagementSystem.py
├── students.csv
├── Output1.png,Output2.png,Output3.png,Output4.png
└── README.md
```

- `StudentManagementSystem.py` contains the Python source code.
- `students.csv` stores student records.
- `Output1.png,Output2.png,Output3.png,Output4.png` shows a screenshot of the program running.
- `README.md` provides information about the project and instructions for running it.



**Author:** Munaza

**Project:** Student Management System using Python