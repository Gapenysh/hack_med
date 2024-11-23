import json
from decimal import Decimal

from psycopg2 import Error
from hack_med.db_connection import connection_db
class DoctorDAL:
    @staticmethod
    def add_doctor_registr():
        pass

    @staticmethod
    def check_doctor_login():
        pass

    @staticmethod
    def get_doctor_rating_and_feedback_count(doctor_id):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT AVG(rating), COUNT(*)
                                  FROM feedback
                                  WHERE doctor_id = %s"""
                cur.execute(stmt, (doctor_id,))
                result = cur.fetchone()
                rating = result
                return rating
        except Error as e:
            return str(e), 0
        finally:
            conn.close()
    @staticmethod
    def get_all_doctors():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT doctor.id, doctor.f_name, doctor.l_name, doctor.m_name, doctor.experience, doctor.address, doctor.price, doctor.photo_url
                      FROM doctor
                      INNER JOIN category ON doctor.category_id = category.id"""
                cur.execute(stmt)
                result = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]

                # Преобразование данных в список словарей
                formatted_data = [
                    dict(zip(colnames, row))
                    for row in result
                ]


                for doctor in formatted_data:
                    doctor_id = doctor['id']
                    avg_rating, feedback_count = DoctorDAL.get_doctor_rating_and_feedback_count(doctor_id)
                    doctor['avg_rating'] = round(avg_rating, 1)
                    doctor['feedback_count'] = feedback_count

                    for doctor in formatted_data:
                        for key, value in doctor.items():
                            if isinstance(value, Decimal):
                                doctor[key] = str(value)

                # Преобразование в JSON
                json_data = json.dumps(formatted_data, ensure_ascii=False, indent=4)
                print(json_data)
                return json_data

                # print(formatted_data)
                # return formatted_data
        except Error as e:
            return str(e)
        finally:
            conn.close()
    @staticmethod
    def get_all_specialities():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt_cat = """SELECT * FROM category"""
                cur.execute(stmt_cat)
                result = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]

                # Преобразование данных в список словарей
                formatted_data = [
                    dict(zip(colnames, row))
                    for row in result
                ]
                # Преобразование в JSON

                json_data = json.dumps(formatted_data, ensure_ascii=False, indent=4)
                print(json_data)
                return json_data
        except Error as e:
            return str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_duty_doctors():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT doctor.id, doctor.f_name, doctor.l_name, doctor.m_name, doctor.experience, doctor.address, doctor.price
                      FROM doctor
                      INNER JOIN category ON doctor.category_id = category.id
                      WHERE doctor.duty = true"""
                cur.execute(stmt)
                result = cur.fetchall()
                # Получение имен столбцов
                colnames = [desc[0] for desc in cur.description]

                # Преобразование данных в список словарей
                formatted_data = [
                    dict(zip(colnames, row))
                    for row in result
                ]
                # Преобразование в JSON



                json_data = json.dumps(formatted_data, ensure_ascii=False, indent=4)
                print(json_data)
                return json_data

        except Error as e:
            return str(e)
        finally:
            conn.close()
    @staticmethod
    def get_info_doctor_by_id(doc_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT *
                              FROM doctor
                              INNER JOIN category ON doctor.category_id = category.id
                              WHERE doctor.id = %s"""
                cur.execute(stmt, (doc_id,))
                result = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                formatted_data = [
                    dict(zip(colnames, row))
                    for row in result
                ]
                # Преобразование в JSON

                json_data = json.dumps(formatted_data, ensure_ascii=False, indent=4)
                print(json_data)
                return json_data
        except Error as e:
            return str(e)
        finally:
            conn.close()
    @staticmethod
    def get_feedbacks_doctor_by_id(doc_id):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT f.id, f.rating, f.detail, c.f_name, c.l_name
                                  FROM feedback f
                                  INNER JOIN client c ON f.client_id = c.id
                                  WHERE doctor_id = %s"""
                cur.execute(stmt, (doc_id,))
                result = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]

                formatted_data = [
                    dict(zip(colnames, row))
                    for row in result
                ]
                # Преобразование в JSON

                print(formatted_data)
                return formatted_data

        except Error as e:
            return str(e)
        finally:
            conn.close()
    @staticmethod
    def get_avg_rating(doc_id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT AVG(rating) FROM feedback
                                WHERE doctor_id = %s"""
                cur.execute(stmt, (doc_id,))
                result = cur.fetchone()

                return result[0]

        except Error as e:
            return str(e)
        finally:
            conn.close()

