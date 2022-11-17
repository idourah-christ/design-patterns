from handlers import HandlerRegistery
from handlers.auth import AuthenficationHandler
from handlers.authorization import AuthorizationHandler
from handlers.country import CountryHandler
from services import AuthentificationService, AuthorizationService

request = {
    'sender': 'www.congo-info.cg',
    'authorization':'read',
    'country':'Congo'
}

auth_data = ['www.congo-info.cg','www.rfi-france.fr','www.france-24.fr']
autho_data = ['read','delete','create']

registery = HandlerRegistery()

registery.append(AuthenficationHandler(AuthentificationService(auth_data)))
registery.append(AuthorizationHandler(AuthorizationService(autho_data)))
registery.append(CountryHandler(['Congo','Mali','Senegal']))



res = registery.run(request)

print(res)
