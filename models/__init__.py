#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

hbhb_storage_type = getenv('HBNB_TYPE_STORAGE')

if hbnb_storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
