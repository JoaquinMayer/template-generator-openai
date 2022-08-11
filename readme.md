Create virtual environment

`python3 -m venv venv`

Activate virtual environment

`source venv/bin/activate`

Install dependencies

`pip install -r requirements.txt`

Create env file

`touch .env`

Add environment variables

OPENAI_API_KEY=<YOUR_API_KEY>

Replaces templates (inside templates folder) and assets (inside assets folder)

Run server

`flask --app app run`