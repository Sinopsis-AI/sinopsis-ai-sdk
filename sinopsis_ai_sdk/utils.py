
from datetime import datetime
import json
from openai import OpenAI
import boto3

def log_user_message(session, user_input, conversationsTable, openai_key):
    timestamp = datetime.utcnow().isoformat()
    session['chat_history'].append({
        "role": "User",
        "user": session['user'],
        "message": user_input,
        "timestamp": timestamp
    })
    update_conversation_in_db(conversationsTable, session, openai_key)

def log_assistant_response(session, assistant_response, chatbot_name, model_name, model_input,conversationsTable, openai_key):
    timestamp = datetime.utcnow().isoformat()
    input_string = json.dumps(model_input)
    session['chat_history'].append({
        "role": "Assistant",
        "message": assistant_response,
        "timestamp": timestamp,
        "chatbot_name": chatbot_name,
        "model_name": model_name,
        "model_input": input_string
    })
    update_conversation_in_db(conversationsTable, session, openai_key)

def update_conversation_in_db(conversationsTable, session, openai_key):
    if 'conversation_id' in session:
        conversation_id = session['conversation_id']
        chat_summary = get_chat_summary(session['chat_history'], openai_key)
        conversationsTable.update_item(
            Key={'conversation_id': conversation_id},
            UpdateExpression='SET #ch = :chat_history, #si = :session_id, #un = :username, #cs = :chat_summary',
            ExpressionAttributeNames={
                '#ch': 'chat_history',
                '#si': 'session_id',
                '#un': 'username',
                '#cs': 'chat_summary'
            },
            ExpressionAttributeValues={
                ':chat_history': session['chat_history'],
                ':session_id': session['session_id'],
                ':username': session['user'],
                ':chat_summary': chat_summary
            }
        )

def get_chat_summary(chat_history, openai_key):
    chat_history_string = " ".join([message['role'] + ': ' + message['message'] for message in chat_history])
    string_dialogue = "You are a helpful assistant. Generate a ~25 word summary of the following conversation: "
    prompt_input = f"{string_dialogue}\n{chat_history_string}"

    client = OpenAI(api_key=openai_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt_input}
        ]
    )

    return completion.choices[0].message.content