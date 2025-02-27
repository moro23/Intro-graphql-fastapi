# Intro to GraphQL with Python & Strawberry

Welcome to the code repository for **Intro to GraphQL with Python & Strawberry**. 
## How to use this repo

The course will walk you step by step on what to do. This codebase is the starting point of your journey!

This project uses Python. In order to build the project locally, run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

To start the server, from the root directory, run:

```bash
uvicorn main:app --reload
```

Right now, the server returns a simple "Hello World" message from `http://localhost:8000`.
