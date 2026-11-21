from pathlib import Path

from pypdf import PdfReader

from backend.schemas.metadata import DocumentMetadata


class MetadataParser:


    def extract(
        self,
        file_path: Path
    ) -> DocumentMetadata:


        reader = PdfReader(
            file_path
        )


        metadata = reader.metadata


        return DocumentMetadata(

            title=(
                metadata.title
                if metadata
                else None
            ),

            author=(
                metadata.author
                if metadata
                else None
            ),

            creator=(
                metadata.creator
                if metadata
                else None
            ),

            producer=(
                metadata.producer
                if metadata
                else None
            ),

            creation_date=(
                str(metadata.creation_date)
                if metadata
                and metadata.creation_date
                else None
            ),

            modification_date=(
                str(metadata.modification_date)
                if metadata
                and metadata.modification_date
                else None
            ),

            page_count=len(
                reader.pages
            ),
        )