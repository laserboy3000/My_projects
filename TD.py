###########################
# Autor: Vladimir Voitov  #
# Date: 07.12.21          # 
# Task: ToDo_list         #
###########################


import sqlite3 #import module for base

class NameExc(Exception): # Create Exception for invalid input task name
    #initialization constructor of class with 3 arg
    def __init__(self, head = "TD_TaskNameError",  message = "Bad name!"):
        super().__init__(message)
        self.head = head
        self.message = message

class PriorityExc(NameExc): # Create Exception for number priority,
                            # with inheritance from NameExc
    #initialization constructor of class with 3 arg
    def __init__(self, head = 'TD_PriorityError', message = "Bad priority!!!"):
        self.head = head
        self.message = message

class IDExc(PriorityExc): # Create Exception for number id,
                          # with inheritans from PriorityExc
    #initialization constructor of class with 3 arg
    def __init__(self, head = 'TD_ID_Error', message = "Bad id!!!"):
        self.head = head
        self.message = message

class Todo: # class creation
    '''
Initialization with creation or open file 'todo.db'
in which we will write tasks
'''
    def __init__(self):
        self.conn = sqlite3.connect('todo.db') # open or creation file
        self.c = self.conn.cursor() # to interact with the database
        self.create_task_table() # for create or open task table

    def create_task_table(self):
        # for create or open(if not found) table with 3 columns (id, name, priority)        
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')
        
    def show_tasks(self):
        # to show all tasks in table
        print("Task table contain the next tasks...") # we cause beauty
        print('ID    | Task name  | Priority') # we cause beauty for 3 column
        for row in self.c.execute('''SELECT * FROM tasks;'''): # call for all tasks in the table
            print(row) # output them all

    def add_task(self):
        # for add task in the table
        task_name = input('Enter task name: ') # ask for name task
        
        if len(task_name) == 0 or task_name.isspace(): # check for correct input
            raise NameExc # call Exception
        res = self.find_task(task_name)
        if res == None: # if all ok
            pass # do nothing
        else:
            # call Exception
            raise NameExc(message = "This name already in tasks!")
        priority = int(input('Enter priority: ')) # ask for input a number
        if priority < 1: # check number, if lower than 0, call Exception
            raise ProrityExc
        # if all OK, add task with 2 parameters
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)',
                       (task_name, priority))
        self.conn.commit() # commit our changes

    def find_task(self, task_name):
        # for find task with name
        self.task_name = task_name

        que = '''SELECT name FROM tasks;''' # ask for all tasks name in the table
        rows = self.c.execute(que) # get list of names
        if (self.task_name in rows) == True: # if find task return it
            return self.task_name
        else:
            return None # if not found, don't return anything

    def update_priority(self):
        # for change priority
        # ask for input priority number 
        priority = int(input('Enter priority number, that will be updated!: '))
        if priority < 1: # if input was not correct
            raise PriorityExc # call for Exception
        # ask number to which we will change
        num_id = int(input('Enter id: '))
        if num_id < 1: # if input was not correct
            raise IdExc # call to Exception

        que = '''UPDATE tasks SET priority = ? WHERE id = ?;'''
        # change priority number
        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?;',
                       (priority, num_id))
        self.conn.commit() # commit our changes

    def delete_task(self):
        # for delete task with id
        num_id = int(input('Enter id which u want to delete: ')) # ask for id
        if num_id < 1 or num_id.isspace(): # check for correct input
            raise IDExc
        
        self.c.execute('''DELETE FROM tasks WHERE id = ?;''', # deleting task
                       (num_id,))
        self.conn.commit() # commit changes

    def exit(self):
        # for exit
        self.conn.close() # close the file


app = Todo() # short name 



def menu_controller(put=0):
    '''
Method for to do some operation with table
'''
    if put == 1:
        #show task service
        app.show_tasks()

    elif put == 2:
        #add task service
        try:
            app.add_task()
        except NameExc as e:
            print(e.message)
        except PriorityExc as e:
            print(e.message)
        except:
            print("Something wrong!")
        else:
            print('The tase was added, my congratulations!!!')
        finally:
            print('tadam')
            
    elif put == 3:
        #Delete task service
        try:
            app.delete_task()
        except IDExc as e:
            print(e.message)
        except:
            print('Something goes wrong :D')
        else:
            print('The task was delete')
        finally:
            print('OoooO')

    elif put == 4:
        #update priority service
        try:
            app.update_priority()
        except PriorityExc as e:
            print(e.message)
        except IDExc as e:
            print(e.message)
        except:
            print('Something wrong....')
        else:
            print('update done!')
        finally:
            print('TaDaM!')

    elif put == 5:
        # for exit
        app.exit()

    else:
        pass


while True:
    print('''
1->_Show Tasks
2->_Add task
3->_Del task
4->_Change Priority
5->_Exit
''')
    try:
        put = int(input("Choose a number from the suggested: "))
        if put == 5:
            menu_controller(put)
            break
    except:
        print("Bad try!!")
    else:
        if put in [1, 2, 3, 4]:
            menu_controller(put)
        
