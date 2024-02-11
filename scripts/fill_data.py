import mysql.connector
from mysql.connector import Error
from faker import Faker
import random

def populate_db():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1111",
            database="testDB"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Генерація даних для груп
            groups = ['A', 'B', 'C']
            for group_name in groups:
                cursor.execute("INSERT INTO `groups` (group_name) VALUES (%s)", (group_name,))

            # Генерація даних для викладачів
            faker = Faker()
            for _ in range(3):
                cursor.execute("INSERT INTO teachers (name, surname, email) VALUES (%s, %s, %s)",
                               (faker.first_name(), faker.last_name(), faker.email()))

            # Генерація предметів
            subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
            cursor.execute("SELECT teacher_id FROM teachers")
            teacher_ids = cursor.fetchall()
            for subject in subjects:
                cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)",
                               (subject, random.choice(teacher_ids)[0]))

            # Генерація студентів
            cursor.execute("SELECT group_id FROM `groups`")
            group_ids = cursor.fetchall()
            for _ in range(50):
                cursor.execute("INSERT INTO students (name, surname, email, group_id) VALUES (%s, %s, %s, %s)",
                               (faker.first_name(), faker.last_name(), faker.email(), random.choice(group_ids)[0]))

            # Генерація оцінок
            cursor.execute("SELECT student_id FROM students")
            student_ids = cursor.fetchall()
            cursor.execute("SELECT subject_id FROM subjects")
            subject_ids = cursor.fetchall()
            for student_id in student_ids:
                for subject_id in subject_ids:
                    for _ in range(random.randint(1, 20)):  # Кількість оцінок для кожного предмета
                        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                                       (student_id[0], subject_id[0], random.randint(1, 10), faker.date()))

            connection.commit()
            print("Database populated with fake data.")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    populate_db()
