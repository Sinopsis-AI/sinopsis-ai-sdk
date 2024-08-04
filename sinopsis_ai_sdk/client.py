from sinopsis_ai_sdk.utils import log_user_message, log_assistant_response, update_conversation_in_db
from datetime import datetime
import boto3

class SinopsisAI:
    def __init__(self, api_key, user="default_user", session_id="default_session", conversation_id="default_conversation"):
        self.api_key = api_key
        self.openai_key = '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'
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.session = {
            "chat_history": [],
            "user": user,  
            "session_id": session_id,
            "conversation_id": conversation_id 
        }

        # Initialize DynamoDB resource and table
        aws_access_key_id = 'AKIAXW3DIR2NQ43Y7RVR'
        aws_secret_access_key = '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'
        self.dynamodb = boto3.resource('dynamodb',
                                       region_name='us-east-1',
                                       aws_access_key_id=aws_access_key_id,
                                       aws_secret_access_key=aws_secret_access_key)
        self.conversationsTable = self.dynamodb.Table('Conversations')

    def log_prompt(self, user_input):
        log_user_message(self.session, user_input, self.conversationsTable, self.openai_key)

    def log_response(self, assistant_response, chatbot_name, model_name, model_input):
        log_assistant_response(self.session, assistant_response, chatbot_name, model_name, model_input, self.conversationsTable, self.openai_key)