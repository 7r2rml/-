from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import uvicorn



# FastAPI 앱 초기화
app = FastAPI()

# CORS 설정
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API 키 설정

client = OpenAI(api_key=api_key)

# 요청 데이터 모델 정의
class TranslateRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

# 번역 API 엔드포인트
@app.post("/translate")
async def translate(req: TranslateRequest):
    prompt = f"Translate the following text from {req.source_lang} to {req.target_lang}: {req.text}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 또는 "gpt-4"
            messages=[
                {"role": "system", "content": "You are a translator."},
                {"role": "user", "content": prompt}
            ]
        )
        translated = response.choices[0].message.content.strip()
        return {"translated_text": translated}
    except Exception as e:
        print("❌ 오류 발생:", e)
        return {"translated_text": f"[ERROR] {str(e)}"}

# 로컬 실행용
if __name__ == "__main__":
    uvicorn.run("backend:app", host="localhost", port=8000, reload=True)
