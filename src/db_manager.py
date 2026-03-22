import sqlite3

class DBManager:
    def __init__(self, db_name='business_data.db'):
        self.db_name = db_name

    def save_to_sql(self, df, table_name='sales_analysis'):
        """Сохранение DataFrame в SQLite"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                df.to_sql(table_name, conn, if_exists='replace', index=False)
            return True
        except Exception as e:
            print(f"Database error: {e}")
            return False