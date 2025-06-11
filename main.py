from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys

def main(prompt):

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # adds turns to list so the model can review the conversation with each prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', # cheaper free tier model
        contents=messages
    )

    # creates verbose output if called
    prompt_token_count = response.usage_metadata.prompt_token_count
    prompt_response_count = response.usage_metadata.candidates_token_count
    if len(sys.argv) > 2:
        argument = sys.argv[2]
        if argument == "--verbose":
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {prompt_response_count}")
    
    # prints response to console
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        main(prompt)
    else:
        sys.exit("Please provide a prompt. Example: python3 main.py \"where all the spice melange at?\"")