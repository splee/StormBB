from stormbb.tests import *

class TestFacebookController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='auth/facebook', action='index'))
        # Test response...
