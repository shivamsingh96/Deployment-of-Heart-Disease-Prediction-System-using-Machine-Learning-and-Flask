# Deployment-of-Heart-Disease-Prediction-System-using-Machine-Learning-and-Flask
In this repository, I have used different Machine Learning algorithms and compare these algorithms based on different evaluation metrics such as accuracy score, recall score and f1-score etc. and later deployed the model using Flask API. 


Flask is a popular Python web framework that can be used for deploying machine learning models as a REST API. This system involves several steps:

1. Data Preprocessing: The first step is to preprocess the data and prepare it for modelling. This includes tasks such as data cleaning, data balancing, and feature selection.

2. Model Training: After data preprocessing, the next step is to train a machine learning model on the prepared data. For a Heart Disease Prediction system, several machine learning algorithms can be used, including Decision Tree, Random Forest, Gradient Boosting, and Extra Gradient Boosting (XGB).

4. Model Evaluation: Once the model is trained, it needs to be evaluated to ensure that it is accurate and robust. The model is evaluated using different evaluation metrics usuch as accuracy score, recall score and f1-score. In which Random Forest outperforms with an accuracy score of 90%.

4. Model Deployment: Once the model is trained and evaluated, it can be deployed as a REST API using Flask. This involves creating a Flask app and defining an endpoint for the model. When a user sends a request to the endpoint with the necessary input parameters, the Flask app will return a prediction based on the machine learning model.

5. User Interface: Finally, a user interface can be created to allow users to interact with the deployed model. This can be done using HTML, CSS, and JavaScript to create a web application that communicates with the Flask API.

Overall, Flask provides a simple and efficient way to deploy the model as a REST API, making it easy for users to access the predictions. The user interface can enhance the user experience by providing an interactive way to access the predictions.


Final Result:

![WhatsApp Image 2023-04-25 at 11 31 47 AM](https://user-images.githubusercontent.com/123630632/235468775-89da2614-0cad-4ba2-88a4-f7e10fd74f11.jpeg)
