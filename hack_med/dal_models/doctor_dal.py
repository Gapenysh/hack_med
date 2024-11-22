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
    def get_all_doctors():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT id, f_name, l_name, m_name, experience, address, price FROM doctor
                INNER JOIN category ON doctor.category_id = category.id"""
                cur.execute()
                result = cur.fetchall()
                return result
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
                cur.execute()
                result = cur.fetchall()
            return result
        except Error as e:
            return str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_duty_doctors():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT id, f_name, l_name, m_name, experience, address, price FROM doctor
                    INNER JOIN category ON doctor.category_id = category.id
                    WHERE duty = true"""
                cur.execute()
                result = cur.fetchall()
                return result
        except Error as e:
            return str(e)
        finally:
            conn.close()
