from ai_engine.embeddings import get_embeddings



def main():

    embeddings = get_embeddings()


    text = """
    ArchAI Reviewer is an AI platform
    that reviews software architecture.
    """


    vector = embeddings.embed_query(text)


    print("\nEmbedding generated successfully")

    print("Vector size:")
    print(len(vector))


    print("\nFirst 5 values:")
    print(vector[:5])



if __name__ == "__main__":
    main()