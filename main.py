from clean_data import clean_xlsx

in_xlsx_path:str = r'phone_numbers.xlsx' # путь к файлу с исходными данными
out_xlsx_path:str = r'phone_numbers_clean.xlsx' # путь к файлу для записи результата

if __name__ == '__main__':
    try:
        result = clean_xlsx(in_xlsx_path,out_xlsx_path) == out_xlsx_path
        print('РЕЗУЛЬТАТ:', 'OK' if result else 'неОК')
    except (FileNotFoundError,KeyboardInterrupt) as e:
        print('ОШИБКА: ', e)
    finally:
        print('ОБРАБОТКА ЗАВЕРШЕНА')
