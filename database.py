# Запросы базе данных
import sqlite3
cursor = None
conn = None


def connect():
    global cursor, conn
    conn = sqlite3.connect("task_manager_data.db")
    cursor = conn.cursor()


connect()


def add_events(name):
    cursor.execute('INSERT INTO EVENTS (name) VALUES (?)', (name,))
    conn.commit()


def del_events(name):
    cursor.execute('DELETE FROM EVENTS WHERE name=?', (name,))
    conn.commit()


def add_schedule(event_id, datatime, name):
    cursor.execute('INSERT INTO SCHEDULE VALUES (?, ?, ?)', (event_id, datatime, name))
    conn.commit()
    
