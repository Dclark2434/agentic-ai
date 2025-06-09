from google import genai
import os
from dotenv import load_dotenv
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    prompt_token_count = response.usage_metadata.prompt_token_count
    prompt_response_count = response.usage_metadata.candidates_token_count

    print(response.text)
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {prompt_response_count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        main()
    else:
        sys.exit("Please provide a prompt. Example: python3 main.py \"where all the spice melange at?\"")