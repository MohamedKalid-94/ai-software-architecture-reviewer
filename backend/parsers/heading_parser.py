import re

from pathlib import Path

from pypdf import PdfReader

from backend.schemas.heading import DocumentHeading


class HeadingParser:


    def extract(
        self,
        file_path: Path
    ) -> list[DocumentHeading]:


        reader = PdfReader(
            file_path
        )


        headings = []


        for page_number, page in enumerate(
            reader.pages,
            start=1
        ):

            text = page.extract_text()


            if not text:
                continue


            lines = text.split("\n")


            for line in lines:

                cleaned = line.strip()


                if self.is_heading(cleaned):

                    headings.append(
                        DocumentHeading(
                            title=cleaned,
                            level=self.detect_level(cleaned),
                            page_number=page_number,
                        )
                    )


        return headings



    def is_heading(
        self,
        text: str
    ) -> bool:


        if len(text) < 3:
            return False


        if len(text) > 100:
            return False


        return bool(
            re.match(
                r"^[A-Z0-9][A-Za-z0-9\s\-:]+$",
                text
            )
        )



    def detect_level(
        self,
        text: str
    ) -> int:


        words = len(
            text.split()
        )


        if words <= 5:
            return 1


        return 2