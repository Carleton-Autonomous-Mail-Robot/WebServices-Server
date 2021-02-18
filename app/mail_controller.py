import app

class MailController():
    def __init__(self):
        self.__clients = dict()
        self.__scheduler = Scheduler(self)



    def newClient(self,msg:str)->int:
        while True:
            client = Client()
            if self.exists(client.get_client_ID()) or client.get_client_ID() == 0:
                continue
            self.__clients[client.get_client_ID()] = client
            self.__scheduler.notifyNewClient(client.get_client_ID(),msg)
            return client.get_client_ID()
    

        
    def exists(self,client_id:int)->bool:
        return client_id in self.__clients.keys()

    def getMail(self,client_id:str)->str:
        id = int(client_id)
        if self.exists(id):
            return self.__clients[id].next_message()
        return 'Not Found'
    
    def has_mail(self,client_id:int)->bool:
        return self.__clients[client_id].inbox_size()
    

    '''
        when clients leave Mail the mail is forwarded to the scheduler for processing
        when scheduler leaves mail, the mail is automatically deposited
    '''
    def leaveMail(self,client_id:str, msg:str, isScheduler=False)->bool:
        id = int(client_id)
        if isScheduler and self.exists(id):
            self.__clients[id].leave_message(msg)
            return True
        
        if self.exists(id):
            return self.__scheduler.message_handler(id,msg)
        


