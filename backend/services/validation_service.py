from pathlib import Path
import hashlib
import json

from pypdf import PdfReader


class ValidationService:


    def __init__(self):

        self.registry_path = Path(
            "backend/storage/metadata/documents.json"
        )

        self.registry_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        if not self.registry_path.exists():

            self.registry_path.write_text(
                "{}"
            )


    def generate_file_hash(
        self,
        file_path: Path
    ) -> str:

        sha256 = hashlib.sha256()


        with file_path.open("rb") as file:

            while chunk := file.read(8192):

                sha256.update(chunk)


        return sha256.hexdigest()



    def check_duplicate(
        self,
        file_hash: str
    ) -> bool:


        documents = json.loads(
            self.registry_path.read_text()
        )


        for document in documents.values():

            if document.get("hash") == file_hash:

                return True


        return False



    def validate_pdf(
        self,
        file_path: Path
    ):

        try:

            pdf = PdfReader(
                file_path
            )


            if pdf.is_encrypted:

                return {
                    "valid": False,
                    "reason": "Password-protected PDF detected."
                }


            page_count = len(
                pdf.pages
            )


            if page_count == 0:

                return {
                    "valid": False,
                    "reason": "PDF contains no pages."
                }


            return {
                "valid": True,
                "pages": page_count
            }


        except Exception:

            return {
                "valid": False,
                "reason": "Corrupted PDF file."
            }