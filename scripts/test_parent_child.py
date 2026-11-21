from backend.services.parent_child_service import ParentChildService



def main():

    text = """

    System Architecture Overview

    The application contains frontend,
    backend and AI processing components.

    Backend uses FastAPI.

    AI workflow uses LangGraph.

    """



    service = ParentChildService()



    result = service.create_hierarchy(

        text=text,

        document_id="doc-001",

        filename="architecture.pdf",

        heading="Architecture Overview",

    )


    print("\nPARENT CHUNKS\n")


    for parent in result["parents"]:

        print(parent)



    print("\nCHILD CHUNKS\n")


    for child in result["children"]:

        print(child)



if __name__ == "__main__":

    main()