# 🧠 AI Summarizer – FastAPI + OpenAI

Projekt API w Pythonie, który pobiera treść artykułu ze wskazanego URL-a, a następnie streszcza go w 3 prostych punktach z wykorzystaniem OpenAI GPT.

## 🚀 Jak uruchomić aplikację

### 1. Klonowanie repozytorium
```bash
git clone git@github.com:Annti/ai_summarizer.git
cd ai_summarizer

2. Utwórz środowisko wirtualne (opcjonalnie, ale zalecane)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Instalacja zależności
```bash
pip install -r requirements.txt

4. Skonfiguruj klucz OpenAI
Utwórz plik .env w katalogu głównym projektu i wklej swój klucz API:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

5. Uruchomienie serwera
```bash
uvicorn main:app --reload

🧪 Testowanie API
Otwórz w przeglądarce:

http://127.0.0.1:8000/docs
Tam znajdziesz interaktywne UI do testowania endpointu /summarize.

Przykładowe zapytanie:
json
{
  "url": "https://www.theverge.com/tech/662719/android-material-3-gen-z-iphone"
}
Przykładowa odpowiedź:
json
Kopiuj
Edytuj
{
  "summary": [
    "1. Artykuł opisuje nowy trend w projektowaniu Material 3.",
    "2. Omówiono, jak Android zmienia się, by przyciągnąć młodszych użytkowników.",
    "3. Porównano podejście Google i Apple do UX."
  ]
}

📚 Technologie użyte w projekcie
FastAPI

Uvicorn – serwer ASGI

newspaper3k – ekstrakcja treści z artykułów

OpenAI Python SDK

Pydantic – walidacja danych

.env do konfiguracji klucza API