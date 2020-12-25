from api.PersonalCenter.PersonalCenter import *
class Pam():
    def __init__(self,api_url, **kwargs):
        self.api_url = api_url
        self.personnal = PersonalCenter(self.api_url,**kwargs)
