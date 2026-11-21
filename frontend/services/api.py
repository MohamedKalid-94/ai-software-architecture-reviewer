import requests


BASE_URL = "http://localhost:8000"


def check_backend_health():

    response = requests.get(
        f"{BASE_URL}/api/v1/health",
        timeout=10,
    )

    response.raise_for_status()

    return response.json()



def upload_document(
    uploaded_file,
    progress_callback=None,
):

    files = {

        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type,
        )

    }


    if progress_callback:

        progress_callback(30)


    response = requests.post(
        f"{BASE_URL}/api/v1/upload",
        files=files,
        timeout=120,
    )


    if progress_callback:

        progress_callback(80)


    response.raise_for_status()


    if progress_callback:

        progress_callback(100)


    return response.json()