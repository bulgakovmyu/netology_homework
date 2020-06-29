import os
import sys
from dotenv import load_dotenv, find_dotenv
from zipfile import ZipFile

def load_kaggle_data(path_copied_from_kaggle):
    load_dotenv(find_dotenv())
    kaggle_cmd = path_copied_from_kaggle + " -p  ..//data --force"

    res = os.system(kaggle_cmd)
    if res != 0:
        print('Обращение к источнику не выполнено =(')
        sys.exit(1)

    try:
        zf = ZipFile("..//data//wine-quality.zip", 'r')
        zf.extractall("..//data")
        zf.close()
        os.remove("..//data//wine-quality.zip")
    except FileNotFoundError as e:
        print('Архив не найден!')
        print(e)
        
