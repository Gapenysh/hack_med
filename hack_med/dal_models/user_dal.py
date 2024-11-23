import json
from datetime import date

from hack_med.db_connection import connection_db
from psycopg2 import Error

class UserDAL:
    @staticmethod
    def add_user_registr():
        pass

    @staticmethod
    def check_user_login():
        pass
    @staticmethod
    def get_user_by_id():
        pass

    @staticmethod
    def add_doctor_feedback(client_id, doctor_id, rating, detail, date_f):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """INSERT INTO feedback(rating, detail, doctor_id, client_id, date) VALUES(%s, %s, %s, %s, %s)"""
                cur.execute(stmt, (rating, detail, doctor_id, client_id, date_f))
                conn.commit()
                return True
        except Error as e:
            print(str(e))
            return False
        finally:
            conn.close()

    @staticmethod
    def get_info_one():
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT * FROM client WHERE number = '9274531235'"""
                cur.execute(stmt)


                result = cur.fetchone()
                print(result)
                colnames = [desc[0] for desc in cur.description]
                # colnames = [desc[0] for desc in cur.description]
                formatted_data = dict(zip(colnames, result))
                for key, value in formatted_data.items():
                    if isinstance(value, date):
                        formatted_data[key] = value.isoformat()
        # Преобразование в JSON

                json_data = json.dumps(formatted_data, ensure_ascii=False, indent=4)
                print(json_data)
                return json_data
        except Error as e:
            print(str(e))
            return False
        finally:
            conn.close()