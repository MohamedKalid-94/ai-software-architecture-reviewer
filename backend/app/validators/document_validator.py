from pathlib import Path



ALLOWED_TYPES = [
    "application/pdf"
]


MAX_FILE_SIZE = 10 * 1024 * 1024



def validate_file(file):


    if file.content_type not in ALLOWED_TYPES:

        raise ValueError(
            "Only PDF files are supported"
        )


    file.file.seek(0, 2)

    size = file.file.tell()

    file.file.seek(0)


    if size > MAX_FILE_SIZE:

        raise ValueError(
            "File size exceeds limit"
        )


    return True