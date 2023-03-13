import sys

DATABASE_PATH='punto.csv'   #llama a la base de datos, que es nuestro csv

if 'pytest' in sys.argv[0]:      #si se ejecuta el test, se cambia la ruta de la base de datos
    DATABASE_PATH='tests/puntos_test.csv'
