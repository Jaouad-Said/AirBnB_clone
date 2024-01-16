"""This is file to indecate that the folder is a package."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()