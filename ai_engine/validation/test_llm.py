from ai_engine.llm import get_llm


def main():

    llm = get_llm()

    response = llm.invoke(
        "Explain what an AI architecture reviewer does in one sentence."
    )

    print("\nLLM Response:")
    print(response.content)


if __name__ == "__main__":
    main()