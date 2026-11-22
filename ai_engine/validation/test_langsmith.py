from ai_engine.llm import get_llm



def main():

    llm = get_llm()


    response = llm.invoke(
        """
        Explain why AI architecture reviews
        need evidence-based findings.
        """
    )


    print(response.content)



if __name__ == "__main__":
    main()