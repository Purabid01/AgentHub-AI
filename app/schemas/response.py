from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    summary: str
    action: str

    