from typing import Optional

from fastapi import APIRouter

from services import get_questions_from_service
from schemas import QuestionRequest, QuestionConstructor
from db import connect

router = APIRouter()


@router.post("/question")
def take_question(question: QuestionRequest) -> Optional[QuestionConstructor]:
    saved_count_que = 0
    while question.questions_num != saved_count_que:
        list_que = get_questions_from_service(question.questions_num-saved_count_que)
        with connect.cursor() as c:
            c.execute("SELECT id FROM quiz_question")
            saved_ids = [el[0] for el in c.fetchall()]
            for el in list_que:
                if el.id not in saved_ids:
                    c.execute("INSERT INTO  quiz_question(id, question, answer, created_date) VALUES (%s, %s, %s, %s)",
                              (el.id, el.question, el.answer, el.created_date))
                    saved_count_que += 1
                else:
                    continue
            connect.commit()
    return list_que
