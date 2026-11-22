import pdfplumber


class TableProcessor:


    def extract_tables(self, pdf_path):

        tables = []


        with pdfplumber.open(pdf_path) as pdf:

            for page_number, page in enumerate(
                pdf.pages,
                start=1
            ):

                extracted_tables = (
                    page.extract_tables()
                )


                for table in extracted_tables:

                    tables.append(
                        {
                            "page_number": page_number,
                            "rows": table
                        }
                    )


        return tables