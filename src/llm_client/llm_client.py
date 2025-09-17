import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER").lower()

class LLMClient:
    def __init__(self):
        if LLM_PROVIDER == "openai":
            from openai import OpenAI
            api_key = os.getenv("LLM_API_KEY_OPENAI")
            self.client = OpenAI(api_key=api_key)
            self.provider = "openai"
            self.model = "openai-something-model"  # Replace with actual OpenAI model
        elif LLM_PROVIDER == "gemini":
            from google import genai
            api_key = os.getenv("LLM_API_KEY_GEMINI")
            self.client = genai.Client(api_key=api_key)
            self.provider = "gemini"
            self.model = "gemini-2.5-flash"
        elif LLM_PROVIDER == "dummy":
            self.provider = "dummy"
        else:
            raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")

    def start_chat(self, **kwargs):
        if self.provider == "openai":
            return self.client.chat.completions.create(**kwargs)
        elif self.provider == "gemini":
            from google.genai import types
            instruction = kwargs.get("instruction")
            return self.client.chats.create(model=self.model, config=types.GenerateContentConfig(system_instruction=instruction))
        elif self.provider == "dummy":
            print(kwargs)
            return kwargs
        else:
            raise NotImplementedError

    def send_message(self, chat, message):
        if self.provider == "openai":
            # For OpenAI, you may need to pass messages as a list of dicts
            return chat(messages=[{"role": "user", "content": message}])
        elif self.provider == "gemini":
            return chat.send_message(message)
        elif self.provider == "dummy":
            print(message)
            return message
        else:
            raise NotImplementedError

    def upload_file(self, file_path):
        if self.provider == "openai":
            raise NotImplementedError("File upload not implemented for this provider.")
        elif self.provider == "gemini":
            print(f"Uploading file: {file_path}")
            return self.client.files.upload(file=file_path)
        elif self.provider == "dummy":
            print(f"Dummy upload for file: {file_path}")
            return file_path
        else:
            raise NotImplementedError("File upload not implemented for this provider.")

    def generate_content(self, **kwargs):
        if self.provider == "openai":
            raise NotImplementedError("Content generation not implemented for this provider.")
        elif self.provider == "gemini":
            from google.genai import types
            contents=kwargs.get("contents")
            instruction=kwargs.get("instruction")
            return self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=types.GenerateContentConfig(system_instruction=instruction)
            ).text
        elif self.provider == "dummy":
            print(kwargs)
            return {"text": kwargs}
        else:
            raise NotImplementedError("Content generation not implemented for this provider.")
