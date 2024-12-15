import pymysql.cursors


def get_institute(education):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                institute_select = (
                    """SELECT DISTINCT institute.id_institute, institute.Institute
FROM student
JOIN education ON education.id_education = student.id_education 
JOIN institute ON institute.id_institute=student.id_institute
JOIN study_group ON student.id_study_group = study_group.id_study_group 
WHERE education.Education ='"""
                    + education
                    + """' AND institute.Institute LIKE '%нститут%'
AND study_group.Study_group NOT LIKE '%з%' AND study_group.Study_group NOT LIKE '%в%'
ORDER BY institute.Institute;"""
                )
                cursor.execute(institute_select)
                institutes = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return institutes


def get_groups(fuclty, course, education):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_group = (
                    """SELECT DISTINCT study_group.Study_group, study_group.id_study_group
FROM student
JOIN study_group ON student.id_study_group = study_group.id_study_group 
JOIN education ON student.id_education = education.id_education 
WHERE student.course = """
                    + str(course)
                    + " AND student.id_fuclty = "
                    + str(fuclty)
                    + """ AND 
education.Education='"""
                    + education
                    + """' AND 
study_group.Study_group NOT LIKE '%з%' AND study_group.Study_group NOT LIKE '%в%'
ORDER 
BY study_group.Study_group;"""
                )
                cursor.execute(select_group)
                groups = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return groups


def get_fuclty(institute, education):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_fuclty = (
                    """SELECT DISTINCT fuclty.Fuclty, fuclty.id_fuclty
FROM student
JOIN fuclty ON student.id_fuclty = fuclty.id_fuclty
JOIN education ON student.id_education = education.id_education 
JOIN study_group ON student.id_study_group = study_group.id_study_group 
WHERE student.id_institute ="""
                    + str(institute)
                    + """ AND 
education.Education='"""
                    + education
                    + """' AND 
study_group.Study_group NOT LIKE '%з%' AND study_group.Study_group NOT LIKE '%в%'
ORDER BY fuclty.Fuclty;"""
                )
                cursor.execute(select_fuclty)
                groups = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return groups


def get_institute_from_id(id_institute):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_institute = (
                    """SELECT DISTINCT Institute
FROM institute
WHERE id_institute="""
                    + str(id_institute)
                    + ";"
                )
                cursor.execute(select_institute)
                institute = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    if institute:
        return institute[0]["Institute"]
    else:
        return None


def get_fuclty_from_id(id_fuclty):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_fuclty = (
                    """SELECT DISTINCT Fuclty
FROM fuclty
WHERE id_fuclty="""
                    + str(id_fuclty)
                    + ";"
                )
                cursor.execute(select_fuclty)
                fuclty = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    if fuclty:
        return fuclty[0]["Fuclty"]
    else:
        return None


def get_study_group_from_id(id_study_group):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_study_group = (
                    """SELECT DISTINCT Study_group
FROM study_group
WHERE id_study_group="""
                    + str(id_study_group)
                    + ";"
                )
                cursor.execute(select_study_group)
                group = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    if group:
        return group[0]["Study_group"]
    else:
        return None


def get_student_from_id(id_student):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_student = (
                    """SELECT DISTINCT Student
FROM student
WHERE id_student="""
                    + str(id_student)
                    + ";"
                )
                cursor.execute(select_student)
                student = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    if student:
        return student[0]["Student"]
    else:
        return None


def get_student(group):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_fuclty = (
                    """SELECT DISTINCT student.Student, student.id_student
FROM student
WHERE student.id_study_group="""
                    + str(group)
                    + " ORDER BY student.Student;"
                )
                cursor.execute(select_fuclty)
                groups = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return groups


def get_schedule_url(group_id):
    url = None
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_group = (
                    """SELECT url FROM study_group
WHERE id_study_group = """
                    + str(group_id)
                    + ";"
                )
                cursor.execute(select_group)
                url = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)
    # print(url)
    if url:
        return url[0]["url"]
    else:
        return None


def get_geo(spot):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_institute = (
                    """SELECT latitude, longitude
FROM spot
WHERE Spot='"""
                    + str(spot)
                    + "';"
                )
                cursor.execute(select_institute)
                geo = cursor.fetchall()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    if geo:
        return [geo[0]["latitude"], geo[0]["longitude"]]
    else:
        return None


def insert_lesson(lesson, group_id, student_id, year, month, day):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        # print("Successful connection!")
        # print('#' * 20)

        try:
            with connection.cursor() as cursor:
                lesson_insert = (
                    "INSERT IGNORE INTO lesson (Lesson) VALUES ('" + lesson + "');"
                )
                print(lesson_insert)
                cursor.execute(lesson_insert)
                connection.commit()

                lesson_id_select = (
                    "SELECT id_lesson From lesson WHERE Lesson = '" + lesson + "';"
                )
                print(lesson_id_select)
                cursor.execute(lesson_id_select)
                lesson_id = cursor.fetchall()[0]["id_lesson"]
                print(lesson_id)

                shedule_insert = (
                    "INSERT IGNORE INTO schedule_list (id_lesson, "
                    + "id_study_group, id_student, lesson_date) "
                    "VALUES ("
                    + str(lesson_id)
                    + ", "
                    + str(group_id)
                    + ", "
                    + str(student_id)
                    + ", '"
                    + str(year)
                    + "-"
                    + str(month)
                    + "-"
                    + str(day)
                    + "')"
                )
                print(shedule_insert)
                cursor.execute(shedule_insert)
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)


def get_lessons(group_id):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_id_lesson = (
                    """SELECT DISTINCT id_lesson
FROM schedule_list
WHERE id_study_group ="""
                    + str(group_id)
                    + ";"
                )
                cursor.execute(select_id_lesson)
                id_lessons = cursor.fetchall()
                print(id_lessons)

                lessons = []

                for i in id_lessons:
                    select_lesson = (
                        "SELECT Lesson from lesson Where id_lesson = "
                        + str(i["id_lesson"])
                        + ";"
                    )
                    cursor.execute(select_lesson)
                    buf = cursor.fetchall()
                    lessons.append(buf[0]["Lesson"])

                print(lessons)

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return lessons


def get_lesson_dates(lesson, group_id, date_start):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                # print("in get_lesson_date")
                select_lesson = (
                    """SELECT id_lesson
                FROM lesson
                WHERE Lesson ='"""
                    + lesson
                    + "';"
                )

                # print(select_lesson)
                cursor.execute(select_lesson)
                id_lesson = cursor.fetchall()[0]["id_lesson"]
                # print(id_lesson)

                select = (
                    "SELECT DISTINCT lesson_date "
                    + "FROM schedule_list "
                    + "WHERE id_study_group = "
                    + str(group_id)
                    + " AND id_lesson = "
                    + str(id_lesson)
                    + " AND lesson_date > '"
                    + date_start
                    + "' ORDER BY(lesson_date) ASC;"
                )
                print(select)
                cursor.execute(select)
                buf = cursor.fetchall()

                dates = ["Студент"]

                for date in buf:
                    # print(date['lesson_date'])
                    # datetime.date()
                    # date_normal = (date['lesson_date'].split('-')[2] + "." +
                    #           date['lesson_date'].split('-')[1] + "." +
                    #           date['lesson_date'].split('-')[0])
                    date_normal = (
                        str(date["lesson_date"].day)
                        + "."
                        + str(date["lesson_date"].month)
                        + "."
                        + str(date["lesson_date"].year)
                    )

                    # print(date_normal)
                    dates.append(date_normal)

                print(dates)

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return dates


def get_student_list(dates, group_id, lesson):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Successful connection!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                select_lesson = (
                    """SELECT id_lesson
                                FROM lesson
                                WHERE Lesson ='"""
                    + lesson
                    + "';"
                )

                # print(select_lesson)
                cursor.execute(select_lesson)
                id_lesson = cursor.fetchone()["id_lesson"]

                # print("in get_lesson_date")
                select = (
                    "SELECT Student "
                    + "FROM student "
                    + "WHERE id_study_group ="
                    + str(group_id)
                    + " ORDER BY Student ASC;"
                )

                # print(select_lesson)
                cursor.execute(select)
                students_database = cursor.fetchall()
                students = [[stud["Student"]] for stud in students_database]
                # print(students)
                # print(id_lesson)
                for student in students:
                    # print(student[0])
                    select_id_student = (
                        """SELECT id_student
                        FROM student
                        WHERE Student ='"""
                        + student[0]
                        + "';"
                    )
                    # print(select_id_student)
                    cursor.execute(select_id_student)
                    id_student = cursor.fetchone()["id_student"]
                    # print(id_student)
                    # print(dates)
                    for date in dates:
                        # print(date)
                        select_visiting = (
                            "SELECT id_schedule_list FROM schedule_list WHERE"
                            + " id_lesson = "
                            + str(id_lesson)
                            + " AND id_student = "
                            + str(id_student)
                            + " AND lesson_date = '"
                            + str(date.split(".")[2])
                            + "-"
                            + str(date.split(".")[1])
                            + "-"
                            + str(date.split(".")[0])
                            + "';"
                        )
                        # print(select_visiting)
                        cursor.execute(select_visiting)
                        buf = cursor.fetchone()
                        # print(buf)
                        if buf is None:
                            # print("-")
                            student.append("-")
                        else:
                            # print("+")
                            student.append("+")

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)

    return students


def delete_visiting(lesson, group_id, student_id, year, month, day):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="students",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
        )
        # print("Successful connection!")
        # print('#' * 20)

        try:
            with connection.cursor() as cursor:

                lesson_id_select = (
                    "SELECT id_lesson From lesson WHERE Lesson = '" + lesson + "';"
                )
                print(lesson_id_select)
                cursor.execute(lesson_id_select)
                lesson_id = cursor.fetchall()[0]["id_lesson"]
                print(lesson_id)

                delete_text = (
                    "DELETE FROM schedule_list WHERE id_lesson= "
                    + str(lesson_id)
                    + " AND id_study_group = "
                    + str(group_id)
                    + " AND id_student = "
                    + str(student_id)
                    + " AND lesson_date = '"
                    + str(year)
                    + "-"
                    + str(month)
                    + "-"
                    + str(day)
                    + "';"
                )
                print(delete_text)
                cursor.execute(delete_text)
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed...")
        print(ex)
