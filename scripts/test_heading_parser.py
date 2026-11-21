from pathlib import Path

from backend.parsers.heading_parser import HeadingParser



def main():

    file_path = Path(
        "backend/storage/uploads/sample.pdf"
    )


    parser = HeadingParser()


    headings = parser.extract(
        file_path
    )


    for heading in headings:

        print(
            f"{heading.level}: {heading.title} (Page {heading.page_number})"
        )



if __name__ == "__main__":

    main()