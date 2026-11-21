from pathlib import Path

from backend.services.parsing_service import ParsingService



def main():

    file_path = Path(
        "backend/storage/uploads/sample.pdf"
    )


    parser = ParsingService()


    result = parser.parse_document(
        file_path
    )


    print("\nFILE:")
    print(
        result["filename"]
    )


    print("\nMETADATA:")
    print(
        result["metadata"]
    )


    print("\nHEADINGS:")
    for heading in result["headings"]:
        print(
            heading
        )


    print("\nTABLES:")
    for table in result["tables"]:
        print(
            table
        )


if __name__ == "__main__":
    main()