from pydantic import BaseModel


class Question(BaseModel):
    question: str
    answer: str
    explanation: str
    difficulty: str
    concept: str


class LearningMaterial(BaseModel):
    topic: str
    summary: str
    key_points: list[str]
    questions: list[Question]