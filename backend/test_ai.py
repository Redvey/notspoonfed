from ai_service import generate_learning_material


topic = input("Enter a CS topic: ")

print("\nGenerating structured learning material...\n")

material = generate_learning_material(topic)


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