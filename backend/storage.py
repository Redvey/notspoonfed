import json
from pathlib import Path

from schemas import LearningMaterial


DATA_DIR = Path(__file__).parent.parent / "data"


def save_learning_material(material: LearningMaterial):

    DATA_DIR.mkdir(exist_ok=True)

    filename = material.topic.lower().replace(" ", "_") + ".json"

    file_path = DATA_DIR / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            material.model_dump(),
            file,
            indent=4,
            ensure_ascii=False,
        )

    return file_path
    