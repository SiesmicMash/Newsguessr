from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI(title="Newsguessr Redactor")

# Load the spaCy model once when the server starts (loading is slow, so we
# don't want to do it on every request).
nlp = spacy.load("en_core_web_sm")

# Entity types that can give away which country an article is from.
#   GPE  = countries, cities, states   (e.g. "Canada", "Paris")
#   LOC  = other locations             (e.g. "the Alps")
#   NORP = nationalities, groups       (e.g. "Canadian", "French")
#   FAC  = buildings, airports, etc.   (e.g. "Heathrow")
#   ORG  = organizations              (e.g. "Bundesbank")
#   PERSON, EVENT, LANGUAGE
REDACT_LABELS = {"GPE", "LOC", "NORP", "FAC", "ORG", "PERSON", "EVENT", "LANGUAGE"}


class RedactRequest(BaseModel):
    """Shape of the JSON body the endpoint expects."""
    text: str


class RedactResponse(BaseModel):
    """Shape of the JSON the endpoint returns."""
    redacted_text: str
    removed_terms: list[str]


def redact_text(text: str) -> tuple[str, list[str]]:
    """Replace location-revealing entities with placeholders like [GPE].

    Returns the redacted text and the list of terms that were removed.
    """
    doc = nlp(text)
    pieces = []        # chunks of the output text, joined at the end
    removed = []       # the original words we replaced
    last_end = 0       # where the previous entity ended in the original text

    for ent in doc.ents:
        if ent.label_ in REDACT_LABELS:
            pieces.append(text[last_end:ent.start_char])  # text before the entity
            pieces.append(f"[{ent.label_}]")              # the placeholder
            removed.append(ent.text)
            last_end = ent.end_char

    pieces.append(text[last_end:])  # whatever is left after the last entity
    return "".join(pieces), removed


@app.post("/redact", response_model=RedactResponse)
def redact(req: RedactRequest):
    redacted_text, removed_terms = redact_text(req.text)
    return RedactResponse(redacted_text=redacted_text, removed_terms=removed_terms)


@app.get("/health")
def health():
    return {"status": "ok"}