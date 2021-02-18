import unittest
from app.mail_controller import MailController

class TestClient(unittest.TestCase):

    def test_new_client(self):
        mc = MailController()
        rid = mc.newClient('robot')
        self.assertIsNotNone(rid)

    def test_two_new_clients(self):
        mc = MailController()
        uid = mc.newClient('user')
        rid = mc.newClient('robot')

        self.assertNotEqual(uid,rid)

    def test_robot_mail(self):
        mc = MailController()
        uid = mc.newClient('user')
        rid = mc.newClient('robot')

        self.assertTrue(mc.leaveMail(str(uid),'test'))
        self.assertTrue(mc.has_mail(str(rid)))
        self.assertEqual('test',mc.getMail(str(rid)))
        