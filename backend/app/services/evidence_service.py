from backend.app.models.evidence import Evidence


class EvidenceService:


    def __init__(self):
        self.evidence_store = []


    def create_evidence(self,evidence_data):
        evidence = Evidence(
            id=f"E-{len(self.evidence_store)+1}",
            document_id=evidence_data.document_id,
            page=evidence_data.page,
            section=evidence_data.section,
            content=evidence_data.content
        )

        self.evidence_store.append(evidence)
        return evidence

    def retrieve_evidence(self,document_id):

        return [
            evidence
            for evidence in self.evidence_store
            if evidence.document_id == document_id
        ]

    def generate_citation(self,evidence):

        return {
            "source":
            evidence.document_id,

            "reference":
            f"Page {evidence.page}, Section {evidence.section}",

            "content":
            evidence.content
        }