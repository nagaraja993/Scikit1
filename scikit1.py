# -*- coding: utf-8 -*-
"""Scikit1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11PRSj2Q8JgCL7C1nb7NvXs0FjynAkVQT

# Problem 1
"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
from sklearn.datasets import load_iris
iris = load_iris()


X = iris.data
Y = iris.target

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# create a linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# save the model
filename = 'linear_model.sav'
pickle.dump(regressor, open(filename, 'wb'))

# load the model
load_model = pickle.load(open(filename, 'rb'))

y_pred = load_model.predict(X_test)
print('root mean squared error : ', np.sqrt(
	metrics.mean_squared_error(y_test, y_pred)))

"""# Problem 2"""

# Loading the data
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# reading the dataset
df = pd.read_csv("sample_data/churn.csv")
X = df[['gender', 'StreamingTV', 'SeniorCitizen', 'tenure', 'MonthlyCharges', 'Dependents','Contract','PaymentMethod','PaperlessBilling']]
Y = df[['Churn']]

X.info()

X.isnull().any()

for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])

plt.figure(figsize=(8, 8))
sns.heatmap(X.corr(),
            linewidths=2,
            annot=True)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=2)
rfc = RandomForestClassifier()
svc = SVC()
lc = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# making predictions on the training set
for clf in (rfc, knn, svc,lc):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy score of ",clf.__class__.__name__,"=",
          100*metrics.accuracy_score(y_test, y_pred))

"""# Problem 3"""

# J48 similar to decision tree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# reading the dataset
df = pd.read_csv("sample_data/churn.csv")
X = df[['gender', 'StreamingTV', 'SeniorCitizen', 'tenure', 'MonthlyCharges', 'Dependents','Contract','PaymentMethod','PaperlessBilling']]
Y = df[['Churn']]

for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

J48 = DecisionTreeClassifier()


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# making predictions on the training set

J48.fit(X_train, y_train)
y_pred = J48.predict(X_test)
print("Accuracy score of ",
      100*metrics.accuracy_score(y_test, y_pred))

"""# Problem 4"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
from sklearn.datasets import load_iris
import statsmodels.formula.api as smf

iris = load_iris()


X = iris.data
Y = iris.target

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

from statsmodels.api import OLS
OLS(y_train,X_train).fit().summary()

