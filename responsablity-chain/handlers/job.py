from handlers import Handler

class JobHandler(Handler):

    def __init__(self, data):
        super().__init__(data)

    def execute(self, request, response=None):
        if request['q'] in self.data:
            return {'status':200, request['q']:'found', 'handler-type':'Job'}

        return self.next.execute(request)