import unittest 
from services import AuthentificationService, AuthorizationService

class AuthentificationServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.data = ['www.congo-info.cg','www.hello-tech.com']
        self.authenService = AuthentificationService(self.data)

    def test_authenticate_request_true(self):
        self.request = {'sender':'www.congo-info.cg'}
        self.assertTrue(self.authenService.authenticate(self.request))

    def test_authenticate_false(self):
        self.request = {'sender':'www.congo_info.cg'}
        self.assertFalse(self.authenService.authenticate(self.request))

    def test_authenticate_missing_sender(self):
        self.request = {'not-sender':'www.congo-info.cg'}
        self.assertFalse(self.authenService.authenticate(self.request))

    def test_authenticate_empty_request(self):
        self.request = {}
        self.assertFalse(self.authenService.authenticate(self.request))


class AuthorizationServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.data = ['read','write']
        self.authoService = AuthorizationService(self.data)

    def test_authorize_true(self):
        self.request = {'authorization':'read'}
        self.assertTrue(self.authoService.authorize(self.request))

    def test_authorize_false(self):
        self.request = {'authorization':'delete'}
        self.assertFalse(self.authoService.authorize(self.request))

    def test_missing_field(self):
        self.request = {'auth':'read'}
        self.assertFalse(self.authoService.authorize(self.request))

    def test_empty_request(self):
        self.request = {}
        self.assertFalse(self.authoService.authorize(self.request))

if __name__ == '__main__':
    unittest.main()