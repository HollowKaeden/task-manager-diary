# Запросы базе данных

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


def get_lessons(date):
    lessons = list(map(lambda x: x[0], cursor.execute('''SELECT e.name FROM EVENTS e 
                             INNER JOIN SCHEDULE s
                             ON e.id = s.event_id
                             WHERE s.datatime=?''', (date, )).fetchall()))
    while len(lessons) != 9:
        lessons.insert(0, '')
    return lessons


connect()
print(get_lessons('Понедельник'))