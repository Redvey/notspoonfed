from ollama import chat


def ask_ai(prompt: str) -> str:
    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI tutor for computer science students. "
                    "Give accurate, concise explanations and focus on "
                    "conceptual understanding."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.message.content


if __name__ == "__main__":
    prompt = input("Ask the local AI: ")

    print("\nGenerating...\n")

    answer = ask_ai(prompt)

    print(answer)