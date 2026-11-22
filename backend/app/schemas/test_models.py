from datetime import datetime

from backend.app.models import (
    ProjectSchema,
    DocumentSchema,
    ReviewSchema,
    FindingSchema,
    EvaluationSchema
)



def main():

    project = ProjectSchema(
        id="P001",
        name="ArchAI Demo Project",
        owner_id="USER001",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )


    print(project)


if __name__ == "__main__":
    main()