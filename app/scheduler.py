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
        if msg == 'test':
            for robot in self.__robots:
                if not self.__controller.has_mail(robot):
                    self.__controller.leaveMail(robot,msg)
                    return True
        return False
