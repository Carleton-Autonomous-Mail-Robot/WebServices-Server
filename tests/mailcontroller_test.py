import unittest
from app.mail_controller import MailController

class TestMailController(unittest.TestCase):

    def test_new_client(self):
        mc = MailController()
        rid = mc.newClient()
        self.assertIsNotNone(rid)

    def test_two_new_clients(self):
        mc = MailController()
        uid = mc.newClient()
        rid = mc.newClient()

        self.assertNotEqual(uid,rid)

    def test_mail(self):
        mc = MailController()
        uid = mc.newClient()
        rid = mc.newClient()

        self.assertTrue(mc.leaveMail(str(rid),'test'))
        self.assertTrue(mc.leaveMail(str(uid),'test2'))
        self.assertTrue(mc.has_mail(str(rid)))
        self.assertEqual('test',mc.getMail(str(rid)))
        self.assertEqual('test2',mc.getMail(str(uid)))
        