# Email Classifier

This repository contains a **Spam vs. Ham** email classifier built using machine learning techniques. 
Below is a screenshot of the web application in use:

![Spam Email]([spam.png](https://github.com/Osisehh/Email-Classifier/blob/master/images/spam.png))
![Ham Email]([ham.png](https://github.com/Osisehh/Email-Classifier/blob/master/images/ham.png))

## Features

- **Web Interface**: A user-friendly interface built using **Flask** where users can input email text, and the model will predict whether the email is spam or not.
- **Machine Learning Model**: The classifier is built using a **supervised learning** model trained on labeled email data.
- **TF-IDF Vectorization**: The text data is preprocessed and vectorized using the **TF-IDF** technique to capture the importance of words in the emails.
- **Spam Detection**: The model uses advanced techniques to accurately classify emails as spam (❌) or not spam (✅).

## Technologies Used

- **Python**: The programming language used for developing the model and web application.
- **Flask**: Web framework to create the front-end user interface.
- **scikit-learn**: A machine learning library for creating and evaluating the spam classification model.
- **TF-IDF Vectorization**: A method to transform the text data into numerical form to be processed by the model.
- **HTML/CSS**: For designing the user interface.
