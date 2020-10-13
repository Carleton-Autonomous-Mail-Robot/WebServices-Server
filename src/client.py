class Client:

    def __init__(self,clientID):
        self.__clientID = clientID
        self.__messages = []

    def getClientID(self):
        return self.__clientID
    
    def leaveMessage(self,msg):
        self.__messages.append(msg)
    
    def nextMessage(self):
        return self.__messages.pop()
    
