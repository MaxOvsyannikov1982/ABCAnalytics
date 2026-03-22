from src.processor import DataProcessor
from src.db_manager import DBManager
import os

def main():
    print("Starting Data Pipeline...")
    
    # Инициализация
    # Получаем абсолютный путь к папке, где лежит сам файл скрипта
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Склеиваем его с папкой данных
    file_path = os.path.join(BASE_DIR, 'data', 'raw_sales.csv')

    proc = DataProcessor(file_path)
    db = DBManager()

    # Процесс
    processed_data = proc.run_abc_analysis()
    
    if db.save_to_sql(processed_data):
        print("Success! Analysis saved to SQL database.")
    else:
        print("Error during database operation.")

if __name__ == "__main__":
    main()