import pymongo
import os

class MailController():
    def __init__(self):
        self.__mdb = pymongo.MongoClient(os.environ['MONGODB_URI'])
        self.__db = self.__mdb['web_services']
        self.__clients = self.__db['clients']



    def newClient(self,robot=False)->str:
        if robot:
            return str(self.__clients.insert_one({'type':'robot'}).inserted_id)
        return str(self.__clients.insert_one({'type':'user'}).inserted_id)
    

    def getMail(self,client_id:str)->str:
        collections = self.__db.collection_names()
        if client_id in collections:
            all_mail =  self.__db[client_id].find()
            if all_mail.count() == 0:
                return None
            current_mail = all_mail[0]
            self.__db[client_id].delete_one(current_mail)
            return current_mail['message']
        return None
    
    

    '''
        when clients leave Mail the mail is forwarded to the scheduler for processing
        when scheduler leaves mail, the mail is automatically deposited
    '''
    def leaveMail(self,client_id:str, msg:str)->bool:
        self.__db[client_id].insert_one({'message':msg})
            
        

        


