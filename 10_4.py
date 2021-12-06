##########################
# Autor: Vladimir Voitov #
# Date: 06.12.21         #
# Task: HW to L10         #
##########################

from os import strerror

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



class Pizza(): # Get a new class
    # init it with list of pizza(menu)
    list_of_pizza = ['margherita','peperoni','calzone']
    def __init__(self):
        pass

    def add_pizza(self, pizza):
        self.pizza = pizza
        if self.pizza not in self.list_of_pizza:
            self.list_of_pizza.append(self.pizza)
        else:
            print('We are already got it! :)')
        print(self.pizza, ": Succesfully adde to list of pizza!")
        print("List of pizzas:", Pizza.list_of_pizza)

    def remove_pizza(self, pizza):
        self.__pizza_rem = pizza
        if self.__pizza_rem in self.list_of_pizza:
            self.list_of_pizza.remove(self.__pizza_rem)
        else:
            print("We already have not this pizza!")
        print(self.__pizza_rem, "Succesfully removed from list of pizza!")
        print("List of pizzas:", Pizza.list_of_pizza)
               

class Order(Pizza): # class for make order

    def __init__(self):
        super().__init__()
        self.orders = {}
        self.counter = 1
        self.message = ""
        self.__fo = open("pizza_order.txt", "wt")
        self.__fo.close()

    def make_pizza(self, pizza, cheese): # check pizza in menu and how many cheese
        self.mpizza = pizza
        self.__cheese = cheese
        if self.mpizza not in self.list_of_pizza: # if not in list
            raise PizzaError # will be error
        if self.__cheese > 100: # if cheese more than 100
            raise TooMuchCheeseError # will be error
        self.orders[self.counter] = self.mpizza
        print(self.counter, self.orders[self.counter], ":Has succesfully created!")

        try:
            value = self.__cheese
            item =  self.mpizza
            self.orders[self.counter] = (item, value)
            print(self.orders[self.counter])
            self.__fo = open("pizza_order.txt", "wt")
            self.__fo.write(str(self.orders[self.counter]))
            self.__fo.close()
            print("File Succesfully writen!")
        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))

        self.counter += 1

pizzeria = Order()

#Make order
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('margherita', 40), ('mafia', 20)]:
    try:
        pizzeria.make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(ch,  ':', tmce.cheese)
    except PizzaError as pe:
        print(pz, ':', pe.pizza)
print()
print()
#Add pizza
for pz in ["peperoni", "calzone", "mafia", "margherita"]:
    try:
        pizzeria.add_pizza(pz)
    except PizzaError as pe:
        print(pz,':', pe.pizza)

print()
print()
#Remove pizza
for pz in ["peperoni", "calzone", "mafia", "margherita", "blablalal"]:
    try:
        pizzeria.remove_pizza(pz)
    except PizzaError as pe:
        print(pz, ':', pe.pizza)











        
        if pizza not in self.__menu: # if not in list
            raise PizzaError # will be error
        if cheese > 100: # if cheese more than 100
            raise TooMuchCheeseError # will be error
        print('Pizza ready!') # if all good 

