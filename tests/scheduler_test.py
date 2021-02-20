import unittest
import json
from app.mail_controller import MailController
from app.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def test_constructor(self):
        mc = MailController()
        s = Scheduler(mc)

        self.assertIsNotNone(s)

    def test_mail_works(self):
        mc = MailController()
        s = Scheduler(mc)

        rid = mc.newClient()
        uid = mc.newClient()
        s.notifyNewClient(rid,'robot')
        s.notifyNewClient(uid,'user')
        self.assertTrue(s.message_handler(uid,{'pickup': 'A','destination': 'B','currentLocation': ''}))
        self.assertFalse(s.message_handler(uid,{'pickup': 'C','destination': 'D','currentLocation': ''}))

        self.assertEqual({'pickup': 'A','destination': 'B','currentLocation': ''}, mc.getMail(str(rid)))

