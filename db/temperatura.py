import sqlite3 
from sqlite3 import Error
from connection import create_connection

def insert_temp(data):
    conn = create_connection()
    sql = """ INSERT INTO temperaturas (temp, hora)
                VALUES( ?, ? )
    """

    try: 
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nueva temperatura agregada")
        return True
    except Error as e:
        print("Error al insertar una temperatura: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()