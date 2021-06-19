import unittest
from app.models import Pitch, User
from flask_login import current_user
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_sho = User(
            username='sho', password='123456', email='abc@defg.com')
        self.new_pitch = Pitch(
            pitch_content="This is my pitch", pitch_category='Business', user=self.user_sho)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_content, "This is my pitch")
        self.assertEquals(self.new_pitch.pitch_category, 'Business')
        self.assertEquals(self.new_pitch.user, self.user_sho)
