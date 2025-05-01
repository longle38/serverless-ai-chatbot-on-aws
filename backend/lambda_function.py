import json
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

def lambda_handler(event, context):
    try:
        # Parse input from API Gateway
        body = json.loads(event['body'])
        user_input = body.get('message', '')

        # Call OpenAI ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        # Get chatbot reply
        reply = response['choices'][0]['message']['content']

        # Return result to frontend
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",  # allow frontend to call it
                "Content-Type": "application/json"
            },
            "body": json.dumps({"response": reply})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
