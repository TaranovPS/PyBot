import pymysql


host = '127.0.0.1'
user = 'root'
password = 'Silasveta5'
db_name = 'Basic_SQL'


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    print('Подключено к базе данных')
    cursor = connection.cursor()
except:
    print('С подключением что-то не так!')

