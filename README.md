# Random-Projects
A bunch of fun project done in my spare time



**Project: SONAR Rock vs Mine Prediction**

This script demonstrates the application of a logistic regression model for binary classification using supervised learning techniques. In this scenario, the model is trained to classify sonar signals as either rocks or mines based on certain features extracted from the signals.

Logistic Regression Model:
Logistic regression is a commonly used statistical technique for binary classification. It predicts the probability of occurrence of an event by fitting data to a logistic function. In this script, a logistic regression model is trained to classify sonar signals into two categories: rocks ('R') and mines ('M').

Binary Classification:
Binary classification is a type of supervised learning where the goal is to categorize instances into one of two classes. In this case, the classes are rocks and mines. The logistic regression model learns to differentiate between these two classes based on the features extracted from the sonar signals.

Supervised Learning:
Supervised learning is a machine learning paradigm where the model is trained on labeled data, meaning that the input data is accompanied by corresponding output labels. During training, the model learns to map input features to output labels, enabling it to make predictions on unseen data.

Usage:

Load the dataset into a DataFrame from a CSV file named 'sonar_data.csv'.
Explore descriptive statistics of the dataset, including the shape of the data, class distribution, and mean of features for rocks and mines.
Separate the features (X) and labels (Y) from the dataset.
Split the dataset into training and test sets using the train_test_split function from scikit-learn.
Train a logistic regression model using the training data.
Evaluate the model's performance on both the training and test data using accuracy score.
Make predictions using the trained model. An example instance is provided in the script for demonstration.

Requirements:

numpy
pandas
scikit-learn

Additions:
- Explore and visualize the data to gain insights and identify any patterns or correlations between features.
- Besides accuracy, evaluate the model using other performance metrics such as precision, recall, F1-score, and ROC-AUC score to get a comprehensive understanding of its performance.
- Plot a confusion matrix to visualize the model's predictions and identify any misclassifications.
- Perform hyperparameter tuning to optimize the model's performance. Use techniques like grid search or random search to find the best combination of hyperparameters.
- Implement cross-validation to assess the model's generalization performance and reduce the risk of overfitting. This ensures that the model's performance is robust across different subsets of the data.
- Provide explanations for model predictions using techniques such as feature importance analysis or partial dependence plots. This helps in understanding which features are driving the model's decisions.
- Construct a machine learning pipeline that includes model training, and evaluation steps. This facilitates the reproducibility and scalability of the workflow.
- Develop a user-friendly interface or deploy the model as an API for real-time predictions. This allows users to interact with the model easily and integrate it into other applications.
- Implement error handling mechanisms to gracefully handle exceptions and provide informative error messages to users in case of failures or unexpected scenarios.
- Provide detailed documentation for the script, including information about the dataset, the problem statement, and the steps involved in the workflow. This helps users understand and use the script effectively.
- Write automated tests to validate the functionality of the script and ensure that changes or updates do not introduce regressions.
- Add logging statements throughout the script to track the execution flow, record important events, and debug issues if they occur.




**Project: Tic Tac Toe**

A Python library, which remains agnostic about the possible ways of presenting the game to the user in a graphical form. The library contains the core logic of the game and two artificial players. Then creating a sample front end to collect user input from the keyboard and visualize the game in the console using plain text

To start: $ python -m console

Development:

1. Implement the low-level details of the tic-tac-toe library

      1.0. Model the Tic-Tac-Toe Game Domain: identify the parts that make up the game and implement them using an object-oriented approach. By modeling the domain of the game with immutable objects results in modular and composable code that’s easier to test, maintain, debug, and understand
  
2. Use these to implement a higher-level game front end in a bottom-up fashion

  Resources: 
  
  https://www.youtube.com/watch?v=BHh654_7Cmw&ab_channel=CleverProgrammer
  
  https://realpython.com/tic-tac-toe-ai-python/#demo-tic-tac-toe-ai-player-in-python
              
  Architecture:
  ![image](https://user-images.githubusercontent.com/100158073/196910198-4294e3b5-c787-464b-9d2b-31e5965572fd.png)
  
  File Structure:
  
![image](https://user-images.githubusercontent.com/100158073/196912632-2200e5e9-08b0-4907-86f2-d24cbee77770.png)

frontends/  is to house one or more concrete game implementations. Contains the __main__.py file, making it a runnable Python package from the command line

library/ is the home folder for the game library 

  tic_tac_toe.game/ a scaffolding designed to be extended by front ends
  
  tic_tac_toe.logic/ the building blocks of the game
  
  pyproject.toml file contains the metadata necessary for building and packaging the library


  
**Project: Pokemon**

  Resources: 
  
  https://www.youtube.com/watch?v=4eDeNCk7df0&ab_channel=AiCore
              
  https://www.youtube.com/watch?v=7LgPcWKA1LI&t=3032s&ab_channel=AiCore
