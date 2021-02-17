from random import randrange
import queue

class Client:

    def __init__(self,clientID=None):
        if clientID is None:
            self.__clientID = self.__generate_client_id()
        else:
            self.__clientID = clientID
        self.__messages = queue.Queue()
        

    def __generate_client_id(self):
        return randrange(2147483647)

    def get_client_type(self):
        return self.__ctype

    def get_client_ID(self):
        return self.__clientID
    
    def leave_message(self,msg):
        self.__messages.put(msg)
    
    def next_message(self):
        return self.__messages.get()
