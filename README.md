# Newsguessr

A game where you read a news article and guess which country it's from.

Originally built at **Fall Hacks 2025** by **adamw-git, bhavijtChauhan, drsh07, and me**, where it won **1st place**. Original repo: [adamw-git/news-guess](https://github.com/adamw-git/news-guess)

This repo continues the project. At the hackathon, removing the clues that give the country away (place names, nationalities, and so on) was done by hand. I'm building a Python/FastAPI service that automates it using spaCy named entity recognition.

## How it works

1. Articles are fetched from the Guardian API.
2. Details that reveal the country (country and city names, nationalities, public figures, and so on) are removed from the text.
3. The player reads the redacted article and guesses the country.

## Tech stack

| Area | Technology |
|---|---|
| Frontend | JavaScript, HTML, CSS |
| Article fetching and storage | Node.js, Guardian API |
| Redaction service (in progress) | Python, FastAPI, spaCy |

## Project structure

```
Newsguessr/
  client/         # Game frontend (JS, HTML, CSS)
  data/           # Article data (JSON)
  scripts/        # index.js: fetches articles from the Guardian API
  db.js           # Database code
  backend/        # FastAPI redaction service (in progress)
```

## Running the game

```bash
npm install -g serve
cd client
serve
```

Then open http://localhost:3000 in your browser.

## Fetching articles

1. Install dependencies:

```bash
npm install
```

2. Create a `.env` file in the project root with your [Guardian API key](https://open-platform.theguardian.com/access/):

```
GUARDIAN_API_KEY=INSERT_KEY_HERE
```

3. Run:

```bash
node scripts/index.js
```

This populates the database and the JSON data file with articles from the Guardian API.

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
- [ ] Evaluation: measure how often a redacted article still reveals its country
- [ ] Keyword scoring (TF-IDF) to catch clues that NER misses
- [ ] Leak check that flags articles where a country clue survived
- [ ] Connect the redaction service to the article-fetching script
- [ ] Docker, CI, and deployment

## Credits

Built at Fall Hacks 2025 with [adamw-git](https://github.com/adamw-git), [bhavijtChauhan](https://github.com/bhavijtChauhan), and [drsh07](https://github.com/drsh07). Redaction service by SiesmicMash.
