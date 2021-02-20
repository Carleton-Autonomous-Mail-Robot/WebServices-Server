from app.client import Client
from app.mail_controller import MailController


class Scheduler():
    def __init__(self,mailcontroller:MailController):
        self.__robots = list()
        self.__others = list()
        self.__controller = mailcontroller
        

    def notifyNewClient(self,client_id:int,client_type:str):
        if client_type == 'robot':
            self.__robots.append(client_id)
            return
        self.__others.append(client_id)
    
    '''
        will decide what todo with the message, and deposit the result in the appropriate mailbox
    '''
    def message_handler(self,client_id,msg)->bool:

        try:
            # If message requesting robot service
            if msg["currentLocation"] == "":
                for robot in self.__robots:
                    if not self.__controller.has_mail(robot):
                        self.__controller.leaveMail(robot,msg)
                        return True
                # No available robots
                return False
                
            # If message contains location information    
            else:
                if self.__controller.exists(client_id):
                    self.__controller.leaveMail(client_id,msg)
                return True
                
        except:
            return False
            
    def delete(self, cid)->bool:
        x = 0
        while x < self.__robots:
            if self.__robots[x] == cid:
                self.__robots.remove(cid)
                return True
        while x < self.__others:
            if self.__others[x] == cid:
                self.__others.remove(cid)
                return True
        return False
                
