from pathlib import Path

from backend.parsers.table_parser import TableParser



def main():


    pdf_path = Path(
        "backend/storage/uploads/sample.pdf"
    )


    parser = TableParser()


    tables = parser.extract(
        pdf_path
    )


    for table in tables:

        print(
            f"Page: {table.page_number}"
        )


        for row in table.rows:

            print(row)



if __name__ == "__main__":

    main()