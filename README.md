# 🧠 AI Summarizer – FastAPI + OpenAI

Projekt API w Pythonie, który pobiera treść artykułu ze wskazanego URL-a, a następnie streszcza go w 3 prostych punktach z wykorzystaniem OpenAI GPT.

## 🚀 Jak uruchomić aplikację

### 1. Klonowanie repozytorium
<pre lang="markdown">
git clone git@github.com:Annti/ai_summarizer.git
cd ai_summarizer
</pre>

### 2. Utwórz środowisko wirtualne (opcjonalnie, ale zalecane)
<pre lang="markdown">
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
</pre>

### 3. Instalacja zależności
<pre lang="markdown">
pip install -r requirements.txt
</pre>

### 4. Skonfiguruj klucz OpenAI

Utwórz plik .env w katalogu głównym projektu i wklej swój klucz API:
<pre lang="markdown">
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
</pre>

### 5. Uruchomienie serwera
<pre lang="markdown">
uvicorn main:app --reload
</pre>

### 🧪 Testowanie API
Otwórz w przeglądarce:
<pre lang="markdown">
http://127.0.0.1:8000/docs
</pre>
Tam znajdziesz interaktywne UI do testowania endpointu /summarize.

Przykładowe zapytanie:
<pre lang="markdown">
{
  "url": "https://www.theverge.com/tech/662719/android-material-3-gen-z-iphone"
}
</pre>

Przykładowa odpowiedź:
<pre lang="markdown">
{
  "summary": [
    "1. Artykuł opisuje nowy trend w projektowaniu Material 3.",
    "2. Omówiono, jak Android zmienia się, by przyciągnąć młodszych użytkowników.",
    "3. Porównano podejście Google i Apple do UX."
  ]
}
</pre>

### 📚 Technologie użyte w projekcie
<pre lang="markdown">
* FastAPI

* Uvicorn – serwer ASGI

* newspaper3k – ekstrakcja treści z artykułów (uwaga strony takie jak np. Onet blokuja newspaper3k)

* OpenAI Python SDK

* Pydantic – walidacja danych

* .env do konfiguracji klucza API
</pre>
