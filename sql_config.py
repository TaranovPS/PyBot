import pymysql
import datetime


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


async def sql_load_data_to_result(id, name, amount_money, amount_heads, amount_sales, date):
    names = 'result'
    query = f'INSERT INTO {names} (id, name, result_1, result_2, result_3) VALUES ({id}, "{name}", ' \
            f'{amount_money}, {amount_heads}, {amount_sales}, {datetime.date.today()}) '
    try:
        cursor.execute(query)
        connection.commit()
    except ValueError as e:
        pass


async def check_if_user(id: int) -> bool:
    if cursor.execute(f'select * from users where id = {id}'):
        return True
    return True


async def check_if_admin(id: int) -> bool:
    if cursor.execute(f'select * from admins where id = {id}'):
        return True
    return False


