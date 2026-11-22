import re


class DocumentStructureService:

    def extract_page_metadata(self, pages):

        metadata = []

        for page in pages:

            text = page["text"]

            metadata.append(
                {
                    "page_number": page["page_number"],
                    "character_count": len(text),
                    "word_count": len(text.split())
                }
            )

        return metadata


    def extract_headings(self, pages):

        headings = []

        heading_pattern = re.compile(r"^[A-Z][A-Z0-9\s\-]{3,}$")

        for page in pages:

            for line in page["text"].splitlines():

                line = line.strip()

                if heading_pattern.match(line):

                    headings.append(
                        {
                            "page_number": page["page_number"],
                            "text": line,
                            "level": 1
                        }
                    )

        return headings


    def detect_sections(self, headings):

        sections = []

        for index, heading in enumerate(headings):

            start_page = heading["page_number"]

            if index + 1 < len(headings):
                end_page = headings[index + 1]["page_number"] - 1
            else:
                end_page = start_page

            sections.append(
                {
                    "title": heading["text"],
                    "start_page": start_page,
                    "end_page": end_page
                }
            )

        return sections


    def classify_document(self, headings):

        titles = " ".join(
            heading["text"].lower()
            for heading in headings
        )

        if "architecture" in titles:
            return "Architecture Document"

        if "design" in titles:
            return "Design Document"

        if "requirements" in titles:
            return "Requirements Specification"

        return "General Document"