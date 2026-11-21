from pathlib import Path

from pypdf import PdfReader

from backend.schemas.parsing import ParsedDocument


class PDFParser:


    def parse(
        self,
        file_path: Path
    ) -> ParsedDocument:
        """
        Extract text from PDF.
        """


        reader = PdfReader(
            file_path
        )


        pages_text = []


        for page in reader.pages:

            text = page.extract_text()

            if text:

                pages_text.append(text)


        extracted_text = "\n".join(
            pages_text
        )


        return ParsedDocument(

            filename=file_path.name,

            total_pages=len(
                reader.pages
            ),

            extracted_text=extracted_text,
        )