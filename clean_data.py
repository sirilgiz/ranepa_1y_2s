# Импортируем используемые библиотеки
import os
import pandas as pd
import re

# Функция считывает указанный файл и возвращает его в виде объекта dataframe
def get_xlsx_content(xlsx_path: str):
    if not(xlsx_path and os.path.isfile(xlsx_path)):
        raise FileNotFoundError('Исходный файл не найден или передан пустой путь')
    df = pd.read_excel(xlsx_path)
    return df


# Функция записывает полученный dataframe в указанный xlsx файл
def write_xlsx_content(df: pd.DataFrame, xlsx_path: str) -> str:
    if not xlsx_path:
        raise FileNotFoundError('Невозможно создать выходной файл — задан пустой путь')
    if os.path.isfile(xlsx_path):
        if input(f'ВНИМАНИЕ: Файл {xlsx_path} существует и будет перезаписан. Нажмите [Enter], чтобы продолжить')!= '':
            raise KeyboardInterrupt('Обработка прервана пользователем')
            return
    df.to_excel(xlsx_path, index=False)
    if os.path.isfile(xlsx_path):
        return xlsx_path


# Функция удаляет все нецифровые символы из строки
def remove_nondigit_char_from_str(s: str):
    if not isinstance(s, str):
        return s
    return re.sub(r'\D', '', s)

# Функция получает на вход пути к файлам и запускает обработку
def clean_xlsx(in_xlsx_path: str, out_xlsx_path: str):
    df = get_xlsx_content(in_xlsx_path)
    df_clean = df.map(remove_nondigit_char_from_str)
    return write_xlsx_content(df_clean, out_xlsx_path)
