from hack_med.db_connection import connection_db

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
    def add_feedback(client_id, doctor_id, rating, detail, date):
        conn = connection_db()
