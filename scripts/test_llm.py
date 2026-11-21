from backend.ai.llm import get_llm


def main():

    llm = get_llm()

    response = llm.invoke("Say hello in one sentence.")

    print("=" * 60)
    print("LLM Response")
    print("=" * 60)
    print(response.content)
    print("=" * 60)


if __name__ == "__main__":
    main()