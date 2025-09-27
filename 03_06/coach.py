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

# --- First call: start the conversation ---
response1 = client.responses.create(
    model="o4-mini",   # reasoning model
    input=[
        {"role": "developer", "content": "You are an AI Personal Coach. Provide 3–5 practical steps."},
        {"role": "user", "content": "Help me reduce stress during my work week."}
    ],
    reasoning={"effort": "medium"},  # optional for reasoning models
    max_output_tokens=500,
)

print("\n--- First Response ---")
print(response1.output_text)

# --- Second call: continue the conversation ---
response2 = client.responses.create(
    model="o4-mini",
    input=[
        {"role": "user", "content": "That’s great. Now how can I stay consistent each week?"}
    ],
    previous_response_id=response1.id,  # reuse reasoning items
    reasoning={"effort": "medium"},
    max_output_tokens=500,
)

print("\n--- Follow-up Response ---")
print(response2.output_text)

