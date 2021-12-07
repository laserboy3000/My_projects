############################
# Autor: Vladimir Voitov   #
# Data 07.12.21            #
# Task: CLass Work to L11  #
############################


import sqlite3

conn = sqlite3.connect('hello.db') # create data base file

conn = sqlite3.connect(':memory:') # create base in memory

conn = sqlite3.connect('D:\HWs\L11\hello.db') # ask for open from directory

# import sqlite3

conn = sqlite3.connect('todo.db') # create data base file
c = conn.cursor() # allows any SQL statements
# create a table "tasks" with 3 columns id, name and priority
c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

#insert data to table
c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)',
          ('My first task', 1))
#fix changes
conn.commit()
#close connection
conn.close()

#executemany() for insert more than 1 data to table

conn = sqlite3.connect('todo.db') # create data base file
c = conn.cursor() # allows any SQL statements
# create a table "tasks" with 3 columns id, name and priority
c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

#create list with tuple of data
tasks = [
    ('My first task', 1),
    ('My secind task', 5),
    ('My third task', 10),
]

#insert data to table
c.executemany('INSERT INTO tasks (name, priority) VALUES (?, ?)', tasks)
#fix changes
conn.commit()
#close connection
conn.close()


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)',
                     (name, priority))
        self.conn.commit()

        
    def show_tasks(self):
        print("Task table contain the next tasks...")
        print('ID    | Task name  | Priority')
        for row in self.c.execute('''SELECT * FROM tasks;'''):
            print(row)

app = Todo()

app.add_task()


conn = sqlite3.connect('todo.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM tasks'):
    print(row)
    for it in range(len(row)):
        print(row[it], end = ' \/ ')
    print()
    print()
conn.close()

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('SELECT * FROM tasks')

rows = c.fetchall()

for row in rows:
    print(row)
conn.close()

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('SELECT * FROM tasks')

row = c.fetchone()
print(row)

row = c.fetchone()
print(row)

conn.close()

def show_tasks(self):
    print("Task table contain the next tasks...")
    print('ID    | Task name  | Priority')
    for row in self.c.execute('''SELECT * FROM tasks;'''):
        print(row)

app.show_tasks()

