import os
import logging
import ntpath
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

def get_directory_info(dir_path):
    for root, dirs, files in os.walk(dir_path):
        logging.info("=====================================")
        logging.info(f"Родительский каталог: {root}")

        for dir in dirs:
            logging.info(FileInfo(dir, None, True, root))

        for file in files:
            name, extension = os.path.splitext(file)
            logging.info(FileInfo(name, extension, False, root))

def main():
    # Получение пути до директории из командной строки
    dir_path = input("Введите путь до директории: ")

    # Запуск сбора информации
    get_directory_info(dir_path)

    print("Информация собрана и сохранена в файле directory_info.log")

if __name__ == "__main__":
    main()