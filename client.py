from random import randrange
import queue

class Client:

    def __init__(self,clientID=None):
        if clientID is None:
            self.__clientID = self.__generate_client_id()
        else:
            self.__clientID = clientID

        self.__messages = queue.Queue()


    def __generate_client_id(self)->int:
        return randrange(2147483647)

    def get_client_ID(self):
        return self.__clientID
    
    def leave_message(self,msg:str):
        self.__messages.put(msg)
    
    def next_message(self)->str:
        return self.__messages.get()
    
