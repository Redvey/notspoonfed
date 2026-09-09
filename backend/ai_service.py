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

def generate_from_notes(notes: str) -> LearningMaterial:

    prompt = f"""
You are an expert computer science tutor preparing a student for GATE CSE.

Use the lecture notes below as the primary source.

LECTURE NOTES:
----------------
{notes}
----------------

Create structured learning material from these notes.

Requirements:

- Identify the main topic.
- Give a concise summary.
- Extract the most important key points.
- Generate exactly 3 conceptual questions.
- Questions must be based on concepts present in the notes.
- Include the correct answer.
- Include a short explanation.
- Difficulty must be one of:
  easy, medium, hard.
- For every question, identify the specific concept being tested.
- Do not invent unrelated concepts that are absent from the notes.
"""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise computer science education system. "
                    "Ground your educational content in the supplied notes."
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