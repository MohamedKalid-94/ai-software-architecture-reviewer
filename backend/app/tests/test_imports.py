from backend.app.models import (
    ProjectSchema,
    DocumentSchema,
    ReviewSchema,
    FindingSchema,
    EvaluationSchema
)


from backend.app.schemas import (
    ProjectCreateSchema,
    DocumentUploadSchema,
    ReviewCreateSchema,
    FindingResponseSchema,
    EvaluationResponseSchema
)



def main():

    print("Models imported successfully ✅")

    print("Schemas imported successfully ✅")


if __name__ == "__main__":
    main()