
import sqlite3
from math import *
from sqlite3 import Cursor
from time import *
''' import logging
    FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
    
    logger = logging.getLogger(__name__)
    
    handler = loging.FileHandler('warehouse_log.log', mode = 'w')
    handler.setLevel(loging.DEBUG)
    
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    logger.critical('CRITICAL MESSAGE')
    logger.error('ERROR MESSAGE')
    logger.warning('WARNING MESSAGE')
    logger.info('INGO MESSAGE')
    logger.debug('DEBUG MESSGE')
'''
class IDExc(Exception):  # Create Exception for number id,

    def __init__(self, head='TD_ID_Error', message="Bad id!!!"):
        self.head = head
        self.message = message


class TonsError(Exception):
    def __init__(self, head='TE_warehouse_Errors', message="We can't give u so much."):
        self.head = head
        self.message = message



class ThicknessError(Exception):
    def __init__(self, head='NE_warehouse_Errors', message='We have not this!!'):
        self.head = head
        self.message = message


class MarkError(Exception):
    def __init__(self, head='ME_warehouse_Errors', message='We have not this mark.'):
        self.head = head
        self.message = message

class SheetsError(Exception):
    def __init__(self, head = 'SE_warehouse_Errors', message = "It's can not be lower than zero!!"):
        self.head = head
        self.message = message

class PositionError(Exception):
    def __init__(self, head='PE_warehouse_Errors', message='We have this position.'):
        self.head = head
        self.message = message




class House:

    def __init__(self):
        self.conn = sqlite3.connect('w_house.db')
        self.c = self.conn.cursor()
        self.create_house_table()

    def create_house_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS metal(
        id INTEGER PRIMARY KEY,
        thickness REAL NOT NULL,
        mark TEXT NOT NULL,
        sheets INTEGER NOT NULL,
        tons INTEGER NOT NULL
        );''')


    def show_metal(self):

        print("Table of metal warehouse...")  # we cause beauty
        print('ID  |  Thickness    | Mark of steel  | Sheets | kg ')  # we cause beauty for 3 column
        for row in self.c.execute('''SELECT * FROM metal;'''):  # call for positions in the table
            print(row)  # output them all

    def add_pos(self):
        # for add information in the table
        marks = input('Enter mark of steel: ')  # ask for mark of steel.

        if len(marks) == 0:  # check for correct input
            raise MarkError  # call Exception

        thick = float(input('Enter thickness of sheets: ')) # ask for thickness.

        if thick < 0.1:
            raise ThicknessError

        res = self.find_pos(thick)

        if res != None:
            raise PositionError



        sh = int(input('How many sheets: '))  # ask for number of sheets
        ton = round(3 * thick * 1.5 * 7.85 * sh, 1)

        if sh < 0:
            raise SheetsError


        self.c.execute('INSERT INTO metal (thickness, mark, sheets, tons) VALUES (?, ?, ?, ?)',
                       (thick, marks, sh, ton))
        self.conn.commit()  # commit our changes

    def del_pos(self): # DELETE POSITION FROM TABLE "metal"
        num_id = int(input('Enter id which u want to delete: '))  # ask for id
        if num_id < 1:  # check for correct input
           raise IDExc

        self.c.execute('''DELETE FROM metal WHERE id = ?;''', (num_id, ))
        self.conn.commit()


    def find_pos(self, f_thick):
        self.f_thick = f_thick
        que = '''SELECT thickness FROM 'metal';'''
        rows = self.c.execute(que)
        if self.f_thick in rows:
            return self.f_thick
        else:
            return None

    def update_pos(self):

        sheet = int(input('Enter a number of sheets: '))
        if sheet < 1:
            raise SheetsError

        num_id = int(input('Enter position id: '))
        if num_id < 1:  # if input was not correct
            raise IDExc # call to Exception

        que = '''UPDATE thickness SET sheets = ? WHERE id = ?;'''
        self.c.execute('UPDATE metal SET sheets = ? WHERE id = ?;',
                       (sheet, num_id))
        self.conn.commit()  # commit our changes



    def exit(self):
        # for exit
        self.conn.close()  # close the file


app = House()  # short name


def menu_controller(put=0):
    '''
Method for to do some operation with table
'''
    if put == 1:
        # show task service
        app.show_metal()

    elif put == 2:
        # add task service
        try:
            app.add_pos()
        except MarkError as e:
            print(e.message)
        except TonsError as e:
            print(e.message)
        except SheetsError as e:
            print(e.message)
        except:
            print("Something wrong!")
        else:
            print('my congratulations!!!')
        finally:
            print('tadam')

    elif put == 3:
        # Delete task service
        try:
            app.del_pos()
        except MarkError as e:
            print(e.message)
        except:
            print('Something goes wrong :D')
        else:
            print('This thickness was delete')
        finally:
            print('OoooO')

    elif put == 4:
        # update priority service
        try:
            app.update_pos()
        except PositionError as e:
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
1->_Show Table of marks
2->_Add sheets
3->_Del position
4->_Change number of sheets
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
