from backend.app.services.document_structure_service import (
    DocumentStructureService
)


def test_structure_service():

    service = DocumentStructureService()

    pages = [
        {
            "page_number": 1,
            "text": "SYSTEM ARCHITECTURE\nApplication overview"
        }
    ]

    metadata = service.extract_page_metadata(pages)
    headings = service.extract_headings(pages)
    sections = service.detect_sections(headings)
    document_type = service.classify_document(headings)

    assert metadata[0]["page_number"] == 1
    assert headings[0]["text"] == "SYSTEM ARCHITECTURE"
    assert sections[0]["title"] == "SYSTEM ARCHITECTURE"
    assert document_type == "Architecture Document"

    print("Document structure extraction passed ✅")


if __name__ == "__main__":
    test_structure_service()