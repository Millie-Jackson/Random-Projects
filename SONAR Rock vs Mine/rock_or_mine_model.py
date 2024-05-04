import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn. metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report

# Load dataset into a Dataframe
sonar_data = pd.read_csv('sonar_data.csv', header=None)

# Descriptive Statistics
sonar_data.shape # Rows and Columns
# sonar_data.describe()
sonar_data[60].value_counts() # How many rock and mines 

sonar_data.groupby(60).mean() # Mean of features for Rocks and Mines

# Separate Features and Labels
X = sonar_data.drop(columns=60, axis=1) # Storing all data in X and dropping the 60th column
Y = sonar_data[60] # Storing the 60th column as the label

print(X)
print(Y)

# Training and Test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1) # 10% test set
print(X.shape, X_train.shape, X_test.shape)

# Model Training (Logistic Regression)
model = LogisticRegression()

# Train the model
model.fit(X_train, Y_train)

# Model Evaluation (training data)
#X_train_prediction = model.predict(X_train)
#training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Model Evaluation (test data)
#X_test_prediction = model.predict(X_test)
#test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

###Performance Evaluation###
Y_train_prediction = model.predict(X_train)
Y_test_prediction = model.predict(X_test)

# Accuracy
train_accuracy = accuracy_score(Y_train, Y_train_prediction)
test_accuracy = accuracy_score(Y_test, Y_test_prediction)
print("Accuracy Score (training): {:.2f}".format(train_accuracy)) # 70% is good
print("Accuracy Score (test): {:.2f}".format(test_accuracy)) # 70% is good

# Precision
train_precision = precision_score(Y_train, Y_train_prediction, pos_label='M')
test_precision = precision_score(Y_test, Y_test_prediction, pos_label='M')
print("Precision Score (training): {:.2f}".format(train_precision)) 
print("Precision Score (test): {:.2f}".format(test_precision)) 

# Recall
train_recall = recall_score(Y_train, Y_train_prediction, pos_label='M')
test_recall = recall_score(Y_test, Y_test_prediction, pos_label='M')
print("Recall Score (training): {:.2f}".format(train_recall)) 
print("Recall Score (test): {:.2f}".format(test_recall))

# F1 Score
train_f1 = f1_score(Y_train, Y_train_prediction, pos_label='M')
test_f1 = f1_score(Y_test, Y_test_prediction, pos_label='M')
print("F1 Score (training): {:.2f}".format(train_f1)) 
print("F1 Score (test): {:.2f}".format(test_f1))

# ROC-AUC Score
train_roc_auc = roc_auc_score(Y_train, model.predict_proba(X_train)[:,1])
test_roc_auc = roc_auc_score(Y_test, model.predict_proba(X_test)[:,1])
print("ROC-AUC Score (training): {:.2f}".format(train_roc_auc)) 
print("ROC_AUC Score (test): {:.2f}".format(test_roc_auc))

# Classificaiion Report
print("\Classification Report (training):")
print(classification_report(Y_train, Y_train_prediction))

print("\Classification Report (test):")
print(classification_report(Y_test, Y_test_prediction))

###Predictive System###

# Take a single random instance to see if it predicted correctly
input_data = (0.0762,	0.0666,	0.0481,	0.0394,	0.059,	0.0649,	0.1209,	0.2467,	0.3564,	0.4459,	0.4152,	0.3952,	0.4256,	0.4135,	0.4528,	0.5326,	0.7306,	0.6193,	0.2032,	0.4636,	0.4148,	0.4292,	0.573,	0.5399,	0.3161,	0.2285,	0.6995,	1,	0.7262,	0.4724,	0.5103,	0.5459,	0.2881,	0.0981,	0.1951,	0.4181,	0.4604,	0.3217,	0.2828,	0.243,	0.1979,	0.2444,	0.1847,	0.0841,	0.0692,	0.0528,	0.0357,	0.0085,	0.023,	0.0046,	0.0156,	0.0031,	0.0054,	0.0105,	0.011,	0.0015,	0.0072,	0.0048,	0.0107,	0.0094)
input_data_as_numpy_array = np.asarray(input_data)  # change input_data to a numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1) # Reshape np array for one instance
prediction = model.predict(input_data_reshaped) # Call prediction on instance

print(prediction)

if(prediction[0]=='R'):
  print('The object is a rock')
else:
   print('The object is a mine')

###VISUALISE THE DATA###

# Histograms
plt.figure(figsize=(12, 6))
for i in range (sonar_data.shape[1]):
   plt.subplot(6, 11, i+1)
   plt.hist(sonar_data[i], bins=20, color='purple', alpha=0.7)
   plt.title("Feature {}".format(i+1))
plt.tight_layout()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(sonar_data.iloc[:, :-1].corr(), annot=True, cmap='coolwarm')  # Exclude the last column (string)
plt.title("Correlation Heatmap")

# Boxplots
plt.figure(figsize=(12, 6))
for i in range(sonar_data.shape[1] - 1): # Exclude the last column (string)
   plt.subplot(6, 11, i+1)
   sns.boxplot(x=sonar_data[60], y=sonar_data[i], palette="Set3")
plt.tight_layout()

plt.show()


