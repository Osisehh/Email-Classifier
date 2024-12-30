import pickle
from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the best model and TfidfVectorizer
with open('best_model.pkl', 'rb') as model_file, open('best_tfidf.pkl', 'rb') as tfidf_file:
    model = pickle.load(model_file)
    tfidf = pickle.load(tfidf_file)

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the homepage (form)
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

# Define a route for prediction (when the form is submitted)
@app.route('/predict', methods=['POST'])
def predict():
    # Get the email message from the POST request
    email_message = request.form['message']  # Using form to get the message

    # Transform the email message using the same TF-IDF vectorizer
    email_message_tfidf = tfidf.transform([email_message])

    # Predict whether the message is spam or not using the loaded model
    prediction = model.predict(email_message_tfidf)

    # Return the prediction (0: Not Spam, 1: Spam)
    return render_template('index.html', prediction=prediction[0], message=email_message)

if __name__ == '__main__':
    app.run(debug=True)