from fastapi import HTTPException
import requests

from schemas import QuestionConstructor

def get_questions_from_service(count: int):
    URL = f'https://jservice.io/api/random?count={count}'
    resource = requests.get(URL)
    if resource.status_code == 200:
        all_questions = []
        for el in resource.json():
            all_questions.append(QuestionConstructor.model_validate(el))
        return all_questions
    raise HTTPException(status_code=404, detail="Questions are not found")
