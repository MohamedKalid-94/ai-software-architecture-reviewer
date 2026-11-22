from backend.app.storage.document_storage import DocumentStorage
from backend.app.validators.document_validator import validate_file
from backend.app.services.metadata_service import MetadataService
from backend.app.repositories.document_repository import DocumentRepository

class DocumentService:

    def __init__(self):
        self.storage = DocumentStorage()
        self.metadata_service = MetadataService()
        self.repository = DocumentRepository()

    def upload_document(
        self,
        file,
        project_id
    ):


        # Validate document
        validate_file(file)

        # Store document
        storage_path = self.storage.save_file(
            file
        )

        # Generate metadata
        metadata = self.metadata_service.generate_metadata(
            file,
            storage_path
        )


        metadata["project_id"] = project_id
        metadata["document_type"] = "ARCHITECTURE_DOCUMENT"
        metadata["status"] = "COMPLETED"

        # Create document record

        document = self.repository.create(
            metadata
        )


        return document