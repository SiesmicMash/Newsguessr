# Newsguessr

A game where you read a news article with its identifying details removed and try to work out which story it is.

Originally built at **Fall Hacks 2025** by **adamw-git, bhavijtChauhan, drsh07, and Me**, where it won **1st place**. Original repo: https://github.com/adamw-git/news-guess

This repo continues the project. At the hackathon, removing identifying keywords from scraped articles was done by hand. I'm building a Python/FastAPI backend that automates it using spaCy named entity recognition.

## How it works

1. Articles are scraped from news sources.
2. Identifying details (people, places, organizations, dates) are removed from the text.
3. The player reads the redacted article and guesses the story.

## Tech stack

| Area | Technology |
|---|---|
| Frontend | JavaScript, HTML, CSS, Mapbox |
| Backend | Python, FastAPI |
| NLP | spaCy (named entity recognition) |

## Project structure

```
newsguessr/
  client/     # Game frontend (JS, HTML, CSS)
  backend/    # FastAPI redaction service
```

## Running the redaction service

Requires Python 3.11+.

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs to try the `/redact` endpoint.

Example request body:

```json
{ "text": "Prime Minister Justin Trudeau spoke in Ottawa on Tuesday." }
```

Example response:

```json
{
  "redacted_text": "Prime Minister [PERSON] spoke in [GPE] on [DATE].",
  "removed_terms": ["Justin Trudeau", "Ottawa", "Tuesday"]
}
```

## Running the frontend

Open `client/index.html` in a browser. The map uses a Mapbox public token (`pk.`), which you need to supply yourself. See `client/mapbox.html`.

## Roadmap

- [x] Hackathon version of the game with manual article redaction
- [ ] `/redact` endpoint using spaCy NER
- [ ] Tests for the redaction stage
- [ ] Evaluation set of hand-labeled articles, with precision, recall, and leak-rate metrics
- [ ] Keyword scoring (TF-IDF) to catch story-specific terms that NER misses
- [ ] Leak check that flags articles where something identifying survived
- [ ] Article storage and game endpoints (`GET /articles/random`, `POST /articles/{id}/guess`)
- [ ] Serve the frontend from FastAPI
- [ ] Docker, CI, and deployment

## Credits

Built at [HACKATHON NAME] with [TEAMMATE 1] and [TEAMMATE 2]. Backend extension by [YOUR NAME].