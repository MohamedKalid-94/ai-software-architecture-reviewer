from datetime import datetime


class MetadataService:


    def generate_metadata(
        self,
        file,
        storage_path
    ):

        file.file.seek(0, 2)

        file_size = file.file.tell()

        file.file.seek(0)


        return {

            "filename": file.filename,

            "file_type": file.content_type,

            "file_size": file_size,

            "storage_path": storage_path,

            "uploaded_at": datetime.now(),

            "status": "UPLOADED"

        }