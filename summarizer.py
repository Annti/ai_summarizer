from openai import OpenAI
import os
from newspaper import Article
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def extract_article_text(url: str ) -> str:
    article = Article(url)
    article.download()
    article.parse()

    if not article.text or len(article.text.strip()) < 50:
        raise ValueError("Nie udało się pobrać artykułu.")
    return article.text

def summarize_with_gpt(text: str, max_tokens: int = 512) -> list[str]:
    prompt = f"Streść poniższy artykuł w 3 punktach: \n\n{text[:3000]}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.7,
    )

    content = response.choices[0].message.content.strip()
    return content.split("\n")  # zakładamy, że punkty są w nowych liniach