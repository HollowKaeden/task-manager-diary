# Запросы базе данных
import sqlite3
cursor = None
conn = None


def connect():
    global cursor, conn
    conn = sqlite3.connect("task_manager_data.db")
    cursor = conn.cursor()


def add_events(name):
    cursor.execute('INSERT INTO EVENTS (name) VALUES (?)', (name,))
    conn.commit()


def del_events(name):
    cursor.execute('DELETE FROM EVENTS WHERE name=?', (name,))
    conn.commit()


def add_schedule(event_id, name):
    cursor.execute('INSERT INTO SCHEDULE VALUES (?, ?, ?)', (get_lessons_count(event_id), event_id, name))
    conn.commit()


def get_lessons(date):
    lessons = list(map(lambda x: x[0], cursor.execute('''SELECT s.name FROM EVENTS e 
                             INNER JOIN SCHEDULE s
                             ON e.id = s.event_id
                             WHERE s.event_id=?''', (date, )).fetchall()))
    while len(lessons) != 9:
        lessons.insert(0, '')
    return lessons


def get_day(day):
    return cursor.execute('SELECT name FROM EVENTS WHERE id=?', (day, )).fetchone()[0]


def get_lessons_count(day):
    return len(cursor.execute('SELECT id FROM SCHEDULE WHERE event_id=?', (day, )).fetchall()) + 1


connect()
print(get_lessons_count(1))
print(get_lessons(1))