from flask import Flask, request, jsonify
from your_deepseek_module import get_deepseek_response  # Import the function from your module

app = Flask(__name__)

@app.route('/get_deepseek_response', methods=['POST'])
def deepseek_response():
    data = request.get_json()
    user_input = data.get('user_input')
    if not user_input:
        return jsonify({'error': 'No user input provided'}), 400
    response = get_deepseek_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
