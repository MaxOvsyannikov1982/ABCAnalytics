from src.processor import DataProcessor
from src.db_manager import DBManager

def main():
    print("Starting Data Pipeline...")
    
    # Инициализация
    proc = DataProcessor('data/raw_sales.csv')
    db = DBManager()

    # Процесс
    processed_data = proc.run_abc_analysis()
    
    if db.save_to_sql(processed_data):
        print("Success! Analysis saved to SQL database.")
    else:
        print("Error during database operation.")

if __name__ == "__main__":
    main()