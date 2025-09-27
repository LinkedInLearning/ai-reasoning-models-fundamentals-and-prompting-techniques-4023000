import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# read local .env file
_ = load_dotenv(find_dotenv()) 

# ---- Configuration ----
# Generate an OpenAI API Key at https://platform.openai.com/api-keys
token = os.environ['OPENAI_API_KEY']
if not token:
    raise SystemExit("Error: Missing API key. Set OPENAI_API_KEY.")

# ---- Client ----
client = OpenAI(
    api_key=token
)

# ---- Request ----
try:
    response = client.chat.completions.create(
        model="o4-mini",
        reasoning_effort="medium",  # low | medium | high
        messages=[
            {
                "role": "developer",
                "content": (
                    "You are an AI Personal Coach. "
                    "Provide clear, personalized, practical advice. "
                    "Respond concisely with 3–5 concrete steps."
                ),
            },
            {
                "role": "user",
                "content": "Provide steps I can take to reduce stress during the work week."
            }
        ],
    )

    print("\n--- AI Personal Coach Response ---")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"[Error] API call failed: {e}")
