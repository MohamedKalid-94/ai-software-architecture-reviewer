from backend.parsers.pdf_parser import PDFParser
from backend.parsers.heading_parser import HeadingParser
from backend.parsers.table_parser import TableParser
from backend.parsers.metadata_parser import MetadataParser


class ParsingService:


    def __init__(self):

        self.pdf_parser = PDFParser()

        self.heading_parser = HeadingParser()

        self.table_parser = TableParser()

        self.metadata_parser = MetadataParser()



    def parse_document(
        self,
        file_path
    ):


        document = self.pdf_parser.parse(
            file_path
        )


        headings = self.heading_parser.extract(
            file_path
        )


        tables = self.table_parser.extract(
            file_path
        )


        metadata = self.metadata_parser.extract(
            file_path
        )


        return {

            "filename": document.filename,

            "text": document.extracted_text,

            "headings": headings,

            "tables": tables,

            "metadata": metadata,

        }