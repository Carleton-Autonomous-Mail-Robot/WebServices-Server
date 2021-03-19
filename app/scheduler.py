from app.mail_controller import MailController
import pymongo
import os

class Scheduler():
    def __init__(self):
        self.__controller = MailController()
        self.__mdb = pymongo.MongoClient(os.environ['MONGODB_URI'])
        self.__db = self.__mdb['web_services']
        self.__clients = self.__db['clients']
        

    def get_robot_id(self)->int:
        for id in self.__robot_id_list():
            all_mail =  self.__db[id].find()
            if all_mail.count() == 0:
                return id
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

    def __robot_id_list(self):
        li_of_robot_ids = list()
        li_of_robots = self.__clients.find({'type' : 'robot'})
        
        for client in li_of_robots:
            li_of_robot_ids.append(str(client['_id']))
        
        return li_of_robot_ids


    def __user_id_list(self):
        li_of_user_ids = list()
        li_of_users = self.__clients.find({'type' : 'user'})

        for client in li_of_users:
            li_of_user_ids.append(str(client['_id']))
        
        return li_of_user_ids




    
    '''
        will decide what todo with the message, and deposit the result in the appropriate mailbox
    '''
    def message_handler(self,client_id,msg)->bool:
        id = int(client_id)
        if id in self.__user_id_list():
            return self.__other_msg_controller(client_id,msg)
        elif id in self.__robot_id_list():
            return self.__robot_msg_controller(client_id,msg)
        return False
            

            
