from handlers import Handler


class CountryHandler(Handler):

    def __init__(self, countries):
        super().__init__()
        self.countries = countries

    def execute_next(self, request, response={}):
        
        response['valid-country'] = request['country'] in self.countries

        return self.next.execute_next(request, response)