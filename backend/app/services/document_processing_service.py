from backend.app.processors.pdf_processor import PDFProcessor

from backend.app.processors.table_processor import (
    TableProcessor
)

from backend.app.services.document_structure_service import (
    DocumentStructureService
)



class DocumentProcessingService:


    def __init__(self):

        self.processor = PDFProcessor()

        self.structure = DocumentStructureService()

        self.table_processor = TableProcessor()



    def process_document(
        self,
        document_path
    ):


        pages = self.processor.extract_text(
            document_path
        )


        page_metadata = (
            self.structure.extract_page_metadata(
                pages
            )
        )


        headings = (
            self.structure.extract_headings(
                pages
            )
        )


        sections = (
            self.structure.detect_sections(
                headings
            )
        )


        document_type = (
            self.structure.classify_document(
                headings
            )
        )


        tables = (
            self.table_processor.extract_tables(
                document_path
            )
        )


        return {

            "document_type": document_type,

            "page_count": len(pages),

            "page_metadata": page_metadata,

            "headings": headings,

            "sections": sections,

            "tables": tables,

            "pages": pages

        }