import unittest
import requests_mock
from sinopsis_ai import SinopsisAI  # Adjust this import according to your file structure

class TestSinopsisAI(unittest.TestCase):

    def setUp(self):
        # Setup common variables
        self.api_key = "test_api_key"
        self.ai = SinopsisAI(api_key=self.api_key)

    @requests_mock.Mocker()
    def test_start_session(self, mock):
        # Mock the retrieve_chat_history endpoint
        mock.post(f'{self.ai.backend_url}/retrieve_chat_history', json=[])

        session = self.ai.start_session(user="test_user")
        self.assertIn("user", session)
        self.assertIn("session_id", session)
        self.assertIn("conversation_id", session)
        self.assertEqual(session["user"], "test_user")
        self.assertEqual(len(session["chat_history"]), 0)

    @requests_mock.Mocker()
    def test_end_session(self, mock):
        # Mock the update_conversation_in_db endpoint
        mock.post(f'{self.ai.backend_url}/update_conversation_in_db', json={})
        
        self.ai.start_session(user="test_user")
        result = self.ai.end_session()
        self.assertTrue(result)
        self.assertIsNone(self.ai.session)

    @requests_mock.Mocker()
    def test_log_prompt(self, mock):
        # Mock the update_conversation_in_db endpoint
        mock.post(f'{self.ai.backend_url}/update_conversation_in_db', json={})

        self.ai.start_session(user="test_user")
        self.ai.log_prompt("Hello, world!")

        self.assertEqual(len(self.ai.session["chat_history"]), 1)
        self.assertEqual(self.ai.session["chat_history"][0]["role"], "User")
        self.assertEqual(self.ai.session["chat_history"][0]["message"], "Hello, world!")

    @requests_mock.Mocker()
    def test_log_response(self, mock):
        # Mock the update_conversation_in_db endpoint
        mock.post(f'{self.ai.backend_url}/update_conversation_in_db', json={})

        self.ai.start_session(user="test_user")
        self.ai.log_response("Hi there!", "ChatbotName", "ModelName", {"input": "Hello"})

        self.assertEqual(len(self.ai.session["chat_history"]), 1)
        self.assertEqual(self.ai.session["chat_history"][0]["role"], "Assistant")
        self.assertEqual(self.ai.session["chat_history"][0]["message"], "Hi there!")

if __name__ == "__main__":
    unittest.main()