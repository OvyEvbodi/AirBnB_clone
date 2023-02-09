#!/usr/bin/python3
"""Iinitializes an instance of the ``FileStorage`` class"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
