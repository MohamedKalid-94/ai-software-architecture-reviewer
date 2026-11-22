from enum import Enum



class UploadStatus(str, Enum):

    RECEIVED = "RECEIVED"

    VALIDATING = "VALIDATING"

    UPLOADING = "UPLOADING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"