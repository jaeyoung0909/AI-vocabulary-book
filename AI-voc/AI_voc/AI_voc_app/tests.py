from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Vocabulary, Ability

# Create your tests here.
class VocabularyTest(TestCase):
    # Make the Vocabulary object.
    def setUp(self):
        return Vocabulary.objects.create(word = "example")
    
    # Test the Vocabulary model works well.
    def testValidity(self):
        v = self.setUp()
        self.assertTrue(isinstance(v, Vocabulary))
        self.assertEqual("example", v.word)
    
class AbilityTest(TestCase):
    
    def setUp(self):
        self.word = Vocabulary.objects.create(word = "example")
        self.user = User.objects.create(username = "testUser", password = "testPassword")

    def testValidity(self):
        Ab = Ability.objects.create(word = self.word, user = self.user, ability = 1)
        
        self.assertTrue(isinstance(Ab, Ability))
        self.assertEqual("example", Ab.word.word)
        self.assertEqual("testUser", Ab.user.username)
        self.assertEqual("testPassword", Ab.user.password)
        self.assertEqual(1, Ab.ability)

        try:
            Ab.save()
        except IntegrityError:
            self.fail("Saving a Ability instance failed.")

# Test for user log in.
class logInTest(TestCase):
    # Create new test user.
    def setUp(self):
        self.user = User.objects.create(username = "testuser")
        self.user.set_password("testpwd")
        self.user.save()

    # Verify whether the log in system works properly.
    def testLogIn(self):
        c = Client()
        c.login(username = "testuser", password = "testpwd")
