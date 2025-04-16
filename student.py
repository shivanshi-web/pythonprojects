import csv

# 📂 File path where student data is stored
FILE_PATH = r'C:\Code_Files\Group project\Student information System\student.csv'

# 📝 Function to view student records
def view_records():
    print("\n📌 Student Records:")
    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Display each student's data

# ➕ Function to add a new student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([student_id, name, age, marks])

    print("✅ Student added successfully!")

# ✏️ Function to update a student’s record
def update_student():
    student_id = input("Enter Student ID to update: ")
    students = []

    # Read existing records
    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file, lineterminator='\n')
        students = list(reader)

    # Modify the marks for the selected student ID
    for row in students:
        if row[0] == student_id:
            row[3] = input(f"Enter updated Marks for {row[1]}: ")

    # Save the updated data back to the CSV file
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("✅ Student record updated successfully!")

# ❌ Function to delete a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    students = []

    # Read and filter out the student record
    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        students = [row for row in reader if row[0] != student_id]

    # Write the remaining records back
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("✅ Student record deleted successfully!")

# 🎓 Function to calculate GPA (assuming simple formula)
def calculate_gpa():
    student_id = input("Enter Student ID to calculate GPA: ")
    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                marks = float(row[3])
                gpa = marks / 20  # Adjust formula as needed
                print(f"📌 GPA for {row[1]}: {round(gpa, 2)}")

# 🏆 Function to find class topper
def class_topper():
    top_student = None
    highest_marks = 0

    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            marks = int(row[3])
            if marks > highest_marks:
                highest_marks = marks
                top_student = row

    if top_student:
        print(f"🏆 Class Topper: {top_student[1]} with {highest_marks} marks!")

# 📌 Menu-driven system
while True:
    print("\n📌 Student Information System (SIS)")
    print("1️⃣ View student records")
    print("2️⃣ Add a student")
    print("3️⃣ Update student records")
    print("4️⃣ Delete a student record")
    print("5️⃣ Calculate GPA")
    print("6️⃣ Find class topper")
    print("7️⃣ Exit")

    op = int(input("Enter the operation number: "))

    if op == 1:
        view_records()
    elif op == 2:
        add_student()
    elif op == 3:
        update_student()
    elif op == 4:
        delete_student()
    elif op == 5:
        calculate_gpa()
    elif op == 6:
        class_topper()
    elif op == 7:
        print("👋 Exiting system. Goodbye!")
        break
    else:
        print("❌ Invalid option! Try again.")