from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api", methods=['POST'])
def openai_api():
    data = request.get_json()
    text = data['text']
    import os
    import openai

    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=text,
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        
        return {
            "error": False,
            "data": response
        }
    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)