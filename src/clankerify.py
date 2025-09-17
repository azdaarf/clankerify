from llm_service.llm_service import LlmService
import json

llm_service = LlmService()


def write_cover_letters():

    response = llm_service.write_cover_letter_for_joblistings()

    cover_letters = []
    if response:
        cover_letters = json.loads(response)

    for cover_letter in cover_letters:
        print("*" * 20)
        print(f"Job: {cover_letter['job_name']}")
        print(f"Cover Letter: {cover_letter['cover_letter']}")
        print(f"CV suggestions: {', '.join(cover_letter['cv_suggestions'])}")
        print("*" * 20)


if __name__ == "__main__":
    write_cover_letters()
