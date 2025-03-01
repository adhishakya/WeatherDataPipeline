from db_connection import get_db_connection

def insert_weather_data(data):
    file = open('insert_data.sql','r')
    query = file.read()
    file.close()

    db_conn = get_db_connection()

    if db_conn:
        try:
            cursor = db_conn.cursor()
            cursor.execute(query, data)
            db_conn.commit()
            print('Data inserted successfully.')
        except:
            print(f'Error inserting data.')  
        finally:
            cursor.close()
            db_conn.close()

    else:
        print('Failed to connect to database')