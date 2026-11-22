from backend.app.processors.table_processor import (
    TableProcessor
)


def test_table_processor():

    processor = TableProcessor()

    assert processor is not None

    print(
        "Table processor initialized successfully ✅"
    )


if __name__ == "__main__":

    test_table_processor()