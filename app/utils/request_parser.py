from fastapi import Request, UploadFile, HTTPException
from typing import Optional
from pydantic import ValidationError
from app.schemas.post import PostData  # твоя модель Pydantic


class PostInput:
    def __init__(self, data: PostData, picture: Optional[UploadFile] = None):
        self.data = data
        self.picture = picture


async def parse_request(request: Request) -> PostInput:
    content_type = request.headers.get("Content-Type", "")

    # Обработка JSON-запроса
    if "application/json" in content_type:
        try:
            json_data = await request.json()
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid JSON body")

        try:
            data = PostData(**json_data)
        except ValidationError as e:
            raise HTTPException(
                status_code=400, detail=f"Validation error: {e.errors()}"
            )
        return PostInput(data=data, picture=None)

    # Обработка multipart/form-data
    elif (
        "multipart/form-data" in content_type
        or "application/x-www-form-urlencoded" in content_type
    ):
        try:
            form = await request.form()
            data = PostData(**form)
        except KeyError as e:
            raise HTTPException(status_code=400, detail=f"Missing form field: {str(e)}")
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid multipart/form-data")

        picture = form.get("picture")  # UploadFile | None
        return PostInput(data=data, picture=picture)

    # Неподдерживаемый Content-Type
    else:
        raise HTTPException(status_code=415, detail="Unsupported Content-Type")
