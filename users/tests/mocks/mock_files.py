"""Module for mock uploaded file."""
import os

from django.core.files.uploadedfile import SimpleUploadedFile


def load_file():
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "fixtures/img.jpg")
    with open(file_path, "rb") as img:
        photo = SimpleUploadedFile(
            name="test.png",
            content=img.read(),
            content_type='image/jpeg'
        )
    return photo
