##########################
# Autor: Vladimir Voitov #
# Date: 04.12.21         #
# Task: HW to L9         #
##########################


class Pizza(): # Get a new class
    # init it with list of pizza(menu)
    def __init__(self, menu = ('margherita','peperoni','calzone')):
        self.__menu = menu
        
    def make_pizza(self, pizza, cheese): # check pizza in menu and how many cheese
        if pizza not in self.__menu: # if not in list
            raise PizzaError # will be error
        if cheese > 100: # if cheese more than 100
            raise TooMuchCheeseError # will be error
        print('Pizza ready!') # if all good 


class PizzaError(Exception): # new error
    # if pizza name not in menu return name as 'not in menu'
    def __init__(self, pizza = 'not in menu', message = ''):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError): # another new error
    # if cheese greater than 100 output 'too much cheese!!! u will be fat!!'
    def __init__(self, pizza= 'unknow', cheese = 'too much cheese!!! u will be fat!!', message = ''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

class Order(Pizza): # class for make order

    # create a empty list for order
    def __init__(self):
        self.order = []

    # create elemetns of list order with 2 arg
    def get_order_piz(self, choice_p = 'unknow', choice_c = 101):
        sp = (choice_p, choice_c)
        self.order.append(sp)

    # return order list
    def cooke(self):
        return self.order


# objects for easy peazy )
pzz = Pizza()
oder = Order()
brah = oder.cooke()

while True:
    answer = input('Ready to do youe order?: (y/n)')
    while answer == 'y':
        print('We can give u: margherita, peperoni, calzone.')
        op = input('Whant pizza u want?: ')
        oc = int(input('How many cheese u want?: (not over 100)'))
        oder.get_order_piz(op, oc)
        answer2 = input('Is that all?: (y/n)')
        if answer2 =='y':
            for (pz, ch) in brah:
                try:
                    pzz.make_pizza(pz, ch)
                except TooMuchCheeseError as tmce:
                    print(tmce, ':', tmce.cheese)
                except PizzaError as pe:
                    print(pe, ':', pe.pizza)
            break
        
    else:
        print('bye, bye')
        break
                     


