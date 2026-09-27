from database import connect_db

def get_age():
    while True:
        try:
            age=int(input("Enter student age:")) 

            if age<0:
                print("Age must be grater than 0.")
            else:
                return age
        except ValueError:
            print("Please enter a valid integer for age.")

def get_student_id():
    while True:
        try:
            student_id=int(input("Enter student ID:")) 

            if student_id<=0:
                print("Student ID must be grater than 0.")
            else:
                return student_id
        except ValueError:
            print("Please enter a valid integer for student ID.")

def get_name():
    while True:
        name=input("Enter student name:").strip()

        if len(name)==0:
            print("Name cannot be empty.")
        else:
            return name

def add_student():
    conn=connect_db()
    cursor=conn.cursor()

    name=get_name()
    age=get_age()
    course=input("Enter Course:")

    query="INSERT INTO students (name,age,course) VALUES (%s,%s,%s)"

    values=(name,age,course)

    cursor.execute(query,values)

    conn.commit()

    print("Student added successfully!")

    cursor.close()
    conn.close()

def view_students():
    conn=connect_db()
    cursor=conn.cursor()

    query="SELECT * FROM students"

    cursor.execute(query)

    students=cursor.fetchall()

    for student in students:
        print(student)

    cursor.close()
    conn.close()

def update_student():
    conn=connect_db()
    cursor=conn.cursor()

    student_id=get_student_id()
    name=get_name()
    age=get_age()
    course=input("Enter new Course:")

    query="UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"

    values=(name,age,course,student_id)

    cursor.execute(query,values)

    conn.commit()
    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student ID not found.")

    cursor.close()
    conn.close()

def delete_student():
    conn=connect_db()
    cursor=conn.cursor()

    student_id=get_student_id()

    query="DELETE FROM students where id=%s"

    cursor.execute(query,(student_id,))

    conn.commit()

    if cursor.rowcount>0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")

    cursor.close()
    conn.close()

def search_student():
    conn=connect_db()
    cursor=conn.cursor()

    student_id=get_student_id()

    query="SELECT * FROM students WHERE id=%s"

    cursor.execute(query,(student_id,))

    student=cursor.fetchone()

    if student:
           print("\n===== STUDENT DETAILS =====")
           print("ID:", student[0])
           print("Name:", student[1])
           print("Age:", student[2])
           print("Course:", student[3])           
    else:
        print("Student ID not found.")

    cursor.close()
    conn.close()