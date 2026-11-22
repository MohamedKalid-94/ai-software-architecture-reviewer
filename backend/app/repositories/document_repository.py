from datetime import datetime
import uuid



class DocumentRepository:


    def __init__(self):

        self.documents = []



    def create(self, document):

        document["id"] = str(
            uuid.uuid4()
        )

        document["uploaded_at"] = datetime.now()


        self.documents.append(
            document
        )


        return document



    def get_all(self):

        return self.documents