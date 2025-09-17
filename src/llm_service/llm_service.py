import os
from dotenv import dotenv_values
from llm_client.llm_client import LLMClient
import json


class LlmService:
    def __init__(self):
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.config = dotenv_values(dotenv_path=os.path.join(self.root_dir, "src", "llm_service", ".properties"))
        self.client = LLMClient()

    def write_cover_letter_for_joblistings(self):
        profile_files = get_files_in_directory(os.path.join(self.root_dir, "upload", "profiles", "active"))
        job_listing_files = get_files_in_directory(os.path.join(self.root_dir, "upload", "joblistings"))

        file_names = profile_files + job_listing_files

        uploaded_files = [self.client.upload_file(file_path=fp) for fp in file_names]

        contents = [self.config["LLM_SERVICE_CV_MATCHING_PROMPT"]] + uploaded_files

        contents += job_listing_files

        response = self.client.generate_content(
            contents=contents,
            instruction=self.config["LLM_SERVICE_CV_MATCHING_INSTRUCTIONS"]
        )

        return response

def get_files_in_directory(directory):
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f != ".gitignore"
    ]
