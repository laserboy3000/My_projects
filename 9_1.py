###########################
# Autor: Voitov Vladimir  #
# Date: 03.12.21          # 
# Task: Class Work to L9  #
###########################


class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__qu = []

    def put(self, elem):
        self.__qu.append(elem)

    def get(self):
        val = self.__qu[0]
        del self.__qu[0]
        return val



que = Queue()
que.put(1)
que.put('dog')
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print('Queue error')
