from pathlib import Path

import pdfplumber

from backend.schemas.table import ExtractedTable


class TableParser:


    def extract(
        self,
        file_path: Path
    ) -> list[ExtractedTable]:


        tables = []


        with pdfplumber.open(file_path) as pdf:


            for page_number, page in enumerate(
                pdf.pages,
                start=1
            ):


                extracted_tables = page.extract_tables()


                for table in extracted_tables:


                    if table:

                        cleaned_table = []


                        for row in table:

                            cleaned_row = [
                                cell.strip() if cell else ""
                                for cell in row
                            ]

                            cleaned_table.append(
                                cleaned_row
                            )


                        tables.append(
                            ExtractedTable(
                                page_number=page_number,
                                rows=cleaned_table,
                            )
                        )


        return tables