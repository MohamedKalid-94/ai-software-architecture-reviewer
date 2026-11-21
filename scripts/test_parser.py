from pathlib import Path

from backend.parsers.pdf_parser import PDFParser


def main():

    pdf_path = Path(
        "backend/storage/uploads/sample.pdf"
    )


    parser = PDFParser()


    result = parser.parse(
        pdf_path
    )


    print(
        "Filename:",
        result.filename
    )


    print(
        "Pages:",
        result.total_pages
    )


    print(
        "Text Preview:"
    )


    print(
        result.extracted_text[:500]
    )


if __name__ == "__main__":

    main()