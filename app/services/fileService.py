import aiofiles.os
from fastapi import UploadFile
import uuid
import aiofiles
import os
from app.core.config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS


class FileService:
    @staticmethod
    def _generate_unique_filename(filename: str):
        ext = filename.split(".")[-1]
        return f"{uuid.uuid4().hex}.{ext}"

    @staticmethod
    async def save_uploaded_file(file: UploadFile | None):
        if not file:
            return None

        if not FileService.allowed_file(file.filename):
            return None

        try:
            unique_name = FileService._generate_unique_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, unique_name)

            async with aiofiles.open(path, "wb") as out_file:
                content = await file.read()
                await out_file.write(content)
            return unique_name
        except Exception as e:
            print("Error: ", str(e))

    @staticmethod
    async def delete_file(filename: str):
        try:
            path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.exists(path):
                await aiofiles.os.remove(path)
        except Exception as e:
            print("Error: ", str(e))

    @staticmethod
    def allowed_file(filename: str):
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )
