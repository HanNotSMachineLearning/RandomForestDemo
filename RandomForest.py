# Load Flower dataset for testing purposes
from sklearn.datasets import load_iris

# Load random forest classifier
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load Numpy
import numpy as np

np.random.seed(0)

# Load flower dataset into iris
iris = load_iris()

# Create table for the data
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add species column
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Add training column, used to split up data in training and test data
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# Create trainingdata to train the algorithm
train = df[df['is_train'] == True]

# Create testdata to try the algorithm on
test = df[df['is_train'] == False]

# Specify the features to use(column names)
features = df.columns[:4]

# Convert species names into int
y = pd.factorize(train['species'])[0]

# Create random forest classifier
clf = RandomForestClassifier(n_estimators=25, random_state=0)

# Train the algorithm with the training data
clf.fit(train[features], y)

# Predict the species of the testing data
clf.predict(test[features])

# Can be used to see the probability for each species
clf.predict_proba(test[features])

# Create species name for predicted plants
preds = iris.target_names[clf.predict(test[features])]

# Create crosstab with predicted and actual flowers. Diagonal values are correctly specified, the others aren't
print(pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species']))

# Displays the importance of the feature in predicting the species
print(list(zip(train[features], clf.feature_importances_)))