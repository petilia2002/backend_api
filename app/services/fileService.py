from fastapi import UploadFile
import uuid
import aiofiles
import os
from app.core.config import UPLOAD_FOLDER


class FileService:
    @staticmethod
    def _generate_unique_filename(filename: str):
        ext = filename.split(".")[-1]
        return f"{uuid.uuid4().hex}.{ext}"

    @staticmethod
    async def save_upload_file(file: UploadFile | None):
        if not file:
            return None

        unique_name = FileService._generate_unique_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, unique_name)

        async with aiofiles.open(save_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)

        return unique_name

    @staticmethod
    async def remove_file():
        pass
