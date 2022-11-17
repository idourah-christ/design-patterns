from handlers.auth import AuthenficationHandler
from handlers.authorization import AuthorizationHandler

from services import AuthentificationService, AuthorizationService

request = {
    'sender': 'www.congo-info.cg',
    'authorization':'read'
}

auth_data = ['www.congo-info.cg','www.rfi-france.fr','www.france-24.fr']
autho_data = ['read','delete','create']


head = AuthenficationHandler(AuthentificationService(auth_data))

current = head 

current.next = AuthorizationHandler(AuthorizationService(autho_data))

current = current.next 

res = head.execute_next(request)

print(res)
