import unittest

# THESE TESTS DO NOT NEED TO BE COMPLETE OR REAL CODE
import sys
sys.path.append('..')
import pdb
#pdb.set_trace()
#pdb.set_trace()
from ..administration.profile import ProfileFactory
from ..database import database as db
class TestStringMethods(unittest.TestCase):

    def test_profile_creation(self):
        # This unit test confirms that a new account is created with the right parameter values and is saved to the db properly
        username = "admin"
        password = "admin"
        new_profile = ProfileFactory.create_new_account(username, password)
        db.save_new_profile(new_profile)
        self.assertEqual(username, new_profile.username)
        self.assertEqual(password, new_profile.password)
        #self.assertEqual(default_values_for_profile, new_profile.default_values)
        #self.assertProxyDatabaseReturnedGoodCode()



if __name__ == '__main__':
    unittest.main()