import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, file_path):
        # Читаем файл (укажите нужную кодировку)
        self.df = pd.read_csv(file_path, sep=None, engine='python', encoding='utf-8')
        
        # Словарь соответствия: 'Название в файле': 'Название в коде'
        mapping = {
            'ID': 'id',
            'Товар': 'product',
            'Цена': 'price',
            'Количество': 'quantity',
            'Маржа': 'margin'
        }
        self.df = self.df.rename(columns=mapping)

    def calculate_metrics(self):
        """Расчет выручки и маржинальности"""
        self.df['revenue'] = self.df['quantity'] * self.df['price']
        self.df['margin_val'] = self.df['revenue'] * 0.2  # Допустим, фикс маржа 20%
        return self.df

    def run_abc_analysis(self):
        """Классический ABC-анализ по Парето (80/15/5)"""
        df = self.calculate_metrics().sort_values(by='revenue', ascending=False)
        df['cum_share'] = df['revenue'].cumsum() / df['revenue'].sum()
        
        df['category'] = np.where(df['cum_share'] <= 0.8, 'A',
                         np.where(df['cum_share'] <= 0.95, 'B', 'C'))
        df = df.copy()
        return df