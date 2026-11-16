# Newsguessr

A game where you read a news article with its identifying details removed and try to work out which story it is.

Originally built at **Fall Hacks 2025** by **adamw-git, bhavijtChauhan, drsh07, and me**, where it won **1st place**. Original repo: [adamw-git/news-guess](https://github.com/adamw-git/news-guess)

This repo continues the project. At the hackathon, removing identifying keywords from scraped articles was done by hand. I'm building a Python/FastAPI service that automates it using spaCy named entity recognition.

## How it works

1. Articles are scraped from news sources.
2. Identifying details (people, places, organizations, dates) are removed from the text.
3. The player reads the redacted article and guesses the story.

## Tech stack

| Area | Technology |
|---|---|
| Frontend | JavaScript, HTML, CSS |
| Existing server | Node.js |
| Redaction service (in progress) | Python, FastAPI, spaCy |

## Project structure

```
Newsguessr/
  client/         # Game frontend (JS, HTML, CSS)
  data/           # Article data
  scripts/        # Scripts from the hackathon version
  db.js           # Node database code from the hackathon version
  backend/        # FastAPI redaction service (in progress)
```

## Running the game

```bash
npm install
# [ADD THE COMMAND YOU USE TO START THE APP, e.g. npm start]
```

## Running the redaction service (in progress)

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

## Roadmap

- [x] Hackathon version of the game with manual article redaction
- [ ] `/redact` endpoint using spaCy NER
- [ ] Tests for the redaction stage
- [ ] Evaluation set of hand-labeled articles, with precision, recall, and leak-rate metrics
- [ ] Keyword scoring (TF-IDF) to catch story-specific terms that NER misses
- [ ] Leak check that flags articles where something identifying survived
- [ ] Connect the redaction service to the game's article pipeline
- [ ] Docker, CI, and deployment

## Credits

Built at Fall Hacks 2025 with [adamw-git](https://github.com/adamw-git), [bhavijtChauhan](https://github.com/bhavijtChauhan), and [drsh07](https://github.com/drsh07). Redaction service by SiesmicMash.
