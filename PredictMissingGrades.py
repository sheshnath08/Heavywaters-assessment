import json
from scipy import stats

from sklearn.linear_model import LinearRegression
import numpy as np


class PredictMissingGrades:
    model = None
    training_features = []
    training_class = []

    def __init__(self, training_features, training_class):
        '''Initializing training features and data'''
        self.training_features = training_features
        self.training_class = training_class
        self.model = LinearRegression()

    def train(self):
        '''Training the model'''
        self.model.fit(self.training_features, self.training_class)


    def predict(self, testing_features):
        '''predict the test data'''
        predictions = self.model.predict(testing_features)
        for each_prediction in predictions:
            print(int(each_prediction))


subjects={"English":0,"Physics":1,"Chemistry":2, "ComputerScience":3,"Biology":4,\
        "PhysicalEducation":5, "Economics":6,"Accountancy":7,"BusinessStudies":8,\
        "Mathematics":9,"serial":10}

def get_x(data):
    x=[3]*9;
    for key in data.keys():
        if subjects[key]<=8:
            x[subjects[key]]=data[key]
    return x

def get_y(data):
    for key in data.keys():
        if subjects[key]==9:    #Mathematics
            y=data[key]
    return y


training_features = []
training_class = []
testing_features =[]
# reading trainig data from text files
lines = open('training.json').readlines()

i = 0
for line in lines:
    if i > 0:  # skip empty lines
        json_line = json.loads(line)
        training_features.append(get_x(json_line))
        training_class.append(get_y(json_line))
    else:
        i = i+1

# training_features = np.array(training_features)
# col_mean = stats.nanmean(training_features,axis=0)
# col_mean = np.array(col_mean, dtype=int)
# print col_mean
# #Find indicies that you need to replace
# inds = np.where(np.isnan(training_features))
#
# #Place column means in the indices. Align the arrays using take
# training_features[inds]=np.take(col_mean,inds[1])

# reading test data from text files
i = 0
for line in open('sample-test.in.json'):
    if i > 0:  # skip empty lines
        testing_features.append(get_x(json.loads(line.strip())))
    else:
        i = i + 1

# n = int(input())
# for i in range(n):
#     testing_features.append(get_x(json.loads(input().strip())))

# To test various model
# names = ['DecisionTreeRegressor', 'LinearRegression', 'Ridge', 'Lasso']
#
# clf_list = [DecisionTreeRegressor(),SGDRegressor(),
#             LinearRegression(),
#             Ridge(),
#             Lasso()]

# for name, clf in zip(names, clf_list):
#     print(name)
#     print(cross_val_score(clf, training_features, training_class, cv=5).mean())

model = PredictMissingGrades(training_features, training_class)
model.train()
model.predict(testing_features)
