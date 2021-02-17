from app.client import Client
from app.scheduler import Scheduler

class MailController():
    def __init__(self):
        self.__clients = dict()
        self.__scheduler = Scheduler()



    def newClient(self,msg:str)->int:
        while True:
            client = Client()
            if exists(client.get_client_ID()) or client.get_client_ID() == 0:
                continue
            self.__clients[client.get_client_ID()] = client
            self.__scheduler.notifyNewClient(client.get_client_ID(),msg)
            return client.get_client_ID()
        
    def exists(self,client_id:int)->bool:
        return client_id in self.__clients.keys()

    def getMail(self,client_id:int)->str:
        if self.exists(client_id):
            return self.__clients[client_id].next_message()
        return 'Not Found'
    

    '''
        when clients leave Mail the mail is forwarded to the scheduler for processing
        when scheduler leaves mail, the mail is automatically deposited
    '''
    def leaveMail(self,client_id:int, msg:str, isScheduler=False)->bool:
        if isScheduler and self.exists(client_id):
            self.__clients[client_id].leave_message(msg)
            return True
        
        if self.exists(client_id):
            return self.__scheduler.message_handler(client_id,msg)
        


