from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Where can I find spice on Arrakis?'
)

print(response.text)
prompt_token_count = response.usage_metadata.prompt_token_count
print(f"Prompt tokens: {prompt_token_count}")
prompt_response_count = response.usage_metadata.candidates_token_count
print(f"Response tokens: {prompt_response_count}")