import os

from filewriter import write_to_file


def test_write_to_file():

    test_filename = "test_output.txt"

    test_content = "Test Content For CI"

    write_to_file(
        test_filename,
        test_content
    )

    # check file exists
    assert os.path.exists(test_filename), "File was not created!"

    # check content
    with open(test_filename, "r") as f:

        content = f.read()

        assert content == test_content, "File Content Do Not Match!"