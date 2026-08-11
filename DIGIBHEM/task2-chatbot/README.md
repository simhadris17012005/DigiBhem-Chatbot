# Task-2: Create a Chatbot

AI/ML Internship Task — Digital Bhem

## Overview
A Python chatbot built with the ChatterBot library, served via a FastAPI
backend and a simple glassmorphic HTML/CSS/JS frontend.

## Tech Stack
- Python + ChatterBot (chatbot engine)
- NLTK / spaCy (NLP, used internally by ChatterBot corpus training)
- FastAPI (backend API)
- HTML/CSS/JS (frontend UI)

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # if using spaCy separately
```

## Run (CLI chatbot)
```bash
python chatbot.py
```

## Run (Web app)
```bash
uvicorn app:app --reload
```
Then open http://localhost:8000 in your browser.

## Training Data
Default: ChatterBot's built-in English corpus.
For richer conversations, swap in the Cornell Movie Dialogs Corpus:
https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

## Deployment
Deploy free on Heroku: https://www.heroku.com/
1. Add a `Procfile`: `web: uvicorn app:app --host=0.0.0.0 --port=$PORT`
2. `heroku create digibhem-chatbot`
3. `git push heroku main`
