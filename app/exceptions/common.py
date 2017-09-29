
class CommonExeception(Exception):
    def __init__(self, message, *args,**kwargs):
        self.message = message
        Exception.__init__(self,*args,**kwargs)
