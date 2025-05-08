from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import summarizer

app = FastAPI()

class UrlRequest(BaseModel):
    url: HttpUrl

@app.post("/summarize")
def summarize_article(payload: UrlRequest):
    try:
        text = summarizer.extract_article_text(str(payload.url))
        summary = summarizer.summarize_with_gpt(text)
        return {"summary":summary}
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Błąd serwera")
