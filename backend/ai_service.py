from ollama import chat

from schemas import LearningMaterial


MODEL_NAME = "qwen3:4b"


def generate_learning_material(topic: str) -> LearningMaterial:

    prompt = f"""
You are an expert computer science tutor preparing students for GATE CSE.

Create learning material for this topic:

{topic}

Requirements:

- Give important key points.
- Generate exactly 3 conceptual questions.
- Questions should test understanding, not memorization.
- Include the correct answer.
- Include a short explanation.
- Difficulty must be one of:
  easy, medium, hard.
- For every question, identify the specific concept being tested.
"""

    response = chat(
        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise computer science education system. "
                    "Return structured educational content."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],

        format=LearningMaterial.model_json_schema(),
    )

    return LearningMaterial.model_validate_json(
        response.message.content
    )