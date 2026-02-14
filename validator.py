from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel


class LessonModel(BaseModel):
    lessonNo: str


app = FastAPI()
conn = sqlite3.connect('ncode_questions.db', check_same_thread=False)
cur = conn.cursor()

msg = 'Hi from validator'


def get_solution(lesson_no: str) -> str:
    row = cur.execute(
        'SELECT solution FROM lesson_solution WHERE lesson_no = ?', lesson_no
    )
    res = row.fetchone()
    res = ''.join(res)
    conn.close()
    return res


@app.post('/validator/')
def validator(item: LessonModel):
    lesson_no = item.lessonNo
    solution = get_solution(lesson_no)
    return solution
