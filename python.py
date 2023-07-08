from flask import Flask, request, jsonify
from flask import Flask, render_template, request

import aiml
import os

kernel = aiml.Kernel()
aiml_path = os.path.join(os.path.dirname(__file__), 'chatbot.aiml')  # Path to your AIML file
kernel.learn(aiml_path)


app = Flask(__name__)

# Define the route handler for the root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['message']
    # Process the user message and generate chatbot response
    chatbot_response = process_user_input(user_message)
    return chatbot_response

# API route for processing user messages
@app.route('/process-message', methods=['POST'])
def process_message():
    # Get the user message from the request
    user_message = request.json['message']

    # Process the user message and generate the chatbot response
    chatbot_response = process_user_input(user_message)

    # Return the chatbot response as JSON
    return jsonify({'response': chatbot_response})

# Function to process user input and generate chatbot response
def process_user_input(user_input):
    # Process user input using AIML interpreter
    aiml_response = kernel.respond(user_input)
    return aiml_response
    # Implement your chatbot logic here
    # You can use AIML or API integration based on your requirements
    # For simplicity, let's just return a static response

  

if __name__ == '__main__':
    app.run()
app.debug = True
