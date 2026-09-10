from ai_service import generate_from_notes
from storage import save_learning_material


print("Paste your lecture notes.")
print("Type END on a new line when finished.\n")


lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    lines.append(line)

notes = "\n".join(lines)

if not notes.strip():
    print("No notes provided.")

else:
    print("\nGenerating material from your notes...\n")

    material = generate_from_notes(notes)
    file_path = save_learning_material(material)

    print("TOPIC")
    print(material.topic)

    print("\nSUMMARY")
    print(material.summary)

    print("\nKEY POINTS")

    for point in material.key_points:
        print("-", point)

    print("\nQUESTIONS")

    for index, question in enumerate(material.questions, start=1):

        print(f"\nQuestion {index}")
        print(question.question)

        print("Answer:")
        print(question.answer)

        print("Explanation:")
        print(question.explanation)

        print("Difficulty:")
        print(question.difficulty)

        print("Concept:")
        print(question.concept)
        
print(f"\nSaved to: {file_path}")