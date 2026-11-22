from backend.app.services.upload_status import UploadStatus



def test_upload_status():

    assert (
        UploadStatus.COMPLETED.value
        ==
        "COMPLETED"
    )


if __name__ == "__main__":

    test_upload_status()

    print(
        "Document upload status validation passed ✅"
    )