from datetime import datetime


class Evidence:

    def __init__(
        self,
        id: str,
        document_id: str,
        page: str,
        section: str,
        content: str,
        created_at: datetime | None = None
    ):

        self.id = id
        self.document_id = document_id
        self.page = page
        self.section = section
        self.content = content
        self.created_at = created_at or datetime.utcnow()