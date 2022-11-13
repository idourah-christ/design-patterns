from handlers import Handler 

class DocumentHandler(Handler):
    
    def __init__(self, data):
       super().__init__(data)

    def execute(self, request):
        if request['q'] in self.data:
            return {'status':200, request['q']:'found', 'handler-type':'document'}

        return self.next.execute(request)