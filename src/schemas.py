from datetime import datetime

from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    questions_num: int = Field(ge=1)


class QuestionConstructor(BaseModel):
    id: int
    question: str
    answer: str
    created_date: datetime = datetime.now()
