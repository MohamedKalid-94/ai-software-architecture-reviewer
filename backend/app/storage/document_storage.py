from pathlib import Path
import shutil


class DocumentStorage:


    def __init__(self, storage_path="storage/documents"):

        self.storage_path = Path(storage_path)

        self.storage_path.mkdir(
            parents=True,
            exist_ok=True
        )


    def save_file(self, upload_file):

        file_path = self.storage_path / upload_file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        print(f"Saved file to: {file_path.resolve()}")

        return str(file_path)