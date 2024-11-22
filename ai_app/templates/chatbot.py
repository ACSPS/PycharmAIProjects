from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

api_endpoint = 'http://localhost:11434/api/chat'
messages = []

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    messages.append({'role': 'user', 'content': user_input})

    data = {'model': 'llama3', 'stream': False, 'messages': messages}
    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        response_data = response.json()
        assistant_response = response_data['message']['content']
        messages.append({'role': 'chatbot', 'content': assistant_response})
        return jsonify({'response': assistant_response})
    else:
        return jsonify({'response': 'Failed to get response from Ollama API'}), 500

if __name__ == '__main__':
    app.run(debug=True)
