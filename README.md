# Email Classifier📨
This project is a machine learning-based email classifier that predicts whether an email is spam or not. It uses natural language processing (NLP) techniques and machine learning algorithms to classify emails.

## Introduction 📝
In this project, we developed an email classification model that predicts whether an email is **spam** or **not spam**. The model is deployed using **Flask**, making it easy to interact with via a web interface.

## Screenshots 📸
Below is a screenshot of the web application in use:

![Spam mailt](/images/spam.png)

**Above is a spam email**❌

![Ham mail](/images/ham.png)

**Above is a ham/not spam email**✅

## Features🌟
- **Web Interface**: A user-friendly interface built using **Flask** where users can input email text, and the model will predict whether the email is spam or not.
- **Machine Learning Model**: The classifier is built using a **supervised learning** model trained on labeled email data.
- **TF-IDF Vectorization**: The text data is preprocessed and vectorized using the **TF-IDF** technique to capture the importance of words in the emails.
- **Spam Detection**: The model uses advanced techniques to accurately classify emails as spam (❌) or not spam (✅).

## Technologies Used💻🛠️
- **Flask** 🧰: Web framework used to build the web app.
- **Python** 🐍: The primary programming language used for the project.
- **scikit-learn** ⚙️: Machine learning library used for building and training the classification model.
- **TfidfVectorizer** 🔥: Tool used for converting the email content into a numerical format for machine learning models.
- **HTML/CSS** 💻: Front-end technologies used for designing the user interface.

 ## Installation ⚙️
To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Osisehh/Email-Classifier
   cd Email-Classifier

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
3. **Activate the virtual environment:**
- **On Windows:**
   ```bash
   venv\Scripts\activate
- **On macOS/Linux:**
   ```bash
   source venv/bin/activate
4. **nstall the required dependencies:**
   ```bash
   pip install -r requirements.txt
 ## Usage 🚀
1. **Run the Flask app:**
   ```bash
   python app.py
2. **Open your browser and go to http://127.0.0.1:5000/. You’ll see the email classification form.**
3. **Paste an email message into the form and click the "Classify" button to see if the email is spam or not.**

## License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact 📬
For any inquiries, feel free to reach out to me:

- Email: [osisehirudunoghena@gmail.com]
- LinkedIn: [www.linkedin.com/in/osiseh-irudunoghena]
- Github: [https://github.com/Osisehh]

## Acknowledgments 🙏
- Thanks to the open-source community for providing valuable resources and tools like Flask, scikit-learn, and TfidfVectorizer.
- A special shout-out to Kaggle for their machine learning datasets, which were used to train the model.
