'''
    A class which abstracts and
    handles any JSON related tasks that maybe required
    to be simpler to use

    @Author Gabriel Ciolac
'''
import json
class Message:

    '''
        Takes a raw JSON formated string and converts it into
        a JSON object
    '''
    def __init__(self,msg):
        try:
            self._jsonObject =  json.loads(msg)
            self._validJSON = True
        except:
            self._jsonObject = ''
            self._validJSON = False


    '''
        Pulls the status out of the JSON
        and returns it as a string
    '''
    def getStatus(self):
        return self._jsonObject['status']
    '''
        Object returns a value from the JSON
        returns None if value wasn't found
    '''
    def getAttribute(self,reg):
        if self._jsonObject[reg] is None:
            return #return none
        return self._jsonObject[reg]

    '''
        Passes if JSON was loaded
        implies that string wasn't JSON
        formated if json.load failed

        Reasons: message was encrypted
                 msg isn't JSON formated

        @Author Gabriel Ciolac
    '''
    def isValid(self):
        return self._validJSON

    def returnJSONIFYFromJSON(self):
        pass
    
    

