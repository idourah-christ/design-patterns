

class AuthentificationService:

    def __init__(self, data):
        self.data = data 

    def authenticate(self, request):

        if not len(request):
            return False 

        if 'sender' not in request:
            return False

        return request['sender'] in self.data



class AuthorizationService:

    def __init__(self, data):
        self.data = data 

    def authorize(self, request):

        if not len(request):
            return False 
            
        if 'authorization' not in request:
            return False

        return request['authorization'] in self.data