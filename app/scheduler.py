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

    def get_robot_id(self)->int:
        for robot in self.__robots:
            if not self.__controller.has_mail(robot):
                return robot
        return 0
    

    def __other_msg_controller(self,client_id,msg)->bool:
        if 'drive' in msg:
            self.__controller.leaveMail(self.get_robot_id(), '1,0')
            return True
        return False
    

    def raw_robot_msg_controller(self,client_id,msg):
        self.__controller.leaveMail(self.get_robot_id(), msg)

        

    def __robot_msg_controller(self,client_id,msg)->bool:
        return False
    
    '''
        will decide what todo with the message, and deposit the result in the appropriate mailbox
    '''
    def message_handler(self,client_id,msg)->bool:
        id = int(client_id)
        if id in self.__others:
            return self.__other_msg_controller(client_id,msg)
        elif id in self.__robots:
            return self.__robot_msg_controller(client_id,msg)
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
                
