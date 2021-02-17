import unittest
from app.client import Client

class TestClient(unittest.TestCase):

    def test_constructor(self):
        rand_client = Client()
        seeded_client = Client(1)
        self.assertIsNotNone(rand_client.get_client_ID())
        self.assertEqual(seeded_client.get_client_ID(),1)

    def test_first_in_first_out(self):
        client = Client()
        message1 = "Message 1"
        message2 = "Message 2"
        message3 = "Message 3"
    
        client.leave_message(message1)
        client.leave_message(message2)
        client.leave_message(message3)

        self.assertEqual(client.next_message(),message1)
        self.assertEqual(client.next_message(),message2)
        self.assertEqual(client.next_message(),message3)