from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.naive_bayes import BernoulliNB


class ByteTheCorrectApple:
    count_vect = CountVectorizer(lowercase=False, ngram_range=(1, 2), max_df=0.95)
    tfidf_transformer = TfidfTransformer(use_idf=False)
    train_data = []  # data store for training data, list of strings
    test_data = []  # data store for test data, list of strings
    train_y = []  # data store for target variables for training, list of A(a)pples
    # initializing model
    clf = BernoulliNB(alpha=.06)  # 94

    def __init__(self, train_data, train_y):
        '''initialize training data'''
        self.train_data = train_data
        self.train_y = train_y


    def train_clf(self):
        '''training the classifier'''
        X_train_counts = self.count_vect.fit_transform(train_data)
        X_train_tfidf = self.tfidf_transformer.fit_transform(X_train_counts)

        clf = self.clf.fit(X_train_tfidf, self.train_y)
        return clf

    def predict(self, test_data):
        '''Prediction function'''
        x_test_counts = self.count_vect.transform(test_data)
        x_test_tfidf = self.tfidf_transformer.transform(x_test_counts)

        # predicting answers for test set
        predicted = self.clf.predict(x_test_tfidf)

        for results in predicted:
            print results


train_data = []			# data store for training data, list of strings
test_data = []			# data store for test data, list of strings
train_y = []			# data store for target variables for training, list of A(a)pples

# reading trainig data from text files
for line in open('apple-computers.txt'):
    if len(line.strip())>0:				#skip empty lines
        train_data.append(line.strip().strip('. '))
        train_y.append('computer-company')

for line in open('apple-fruit.txt'):
    if len(line.strip())>0:				#skip empty lines
        train_data.append(line.strip('. '))
        train_y.append('fruit')


model = ByteTheCorrectApple(train_data, train_y)
model.train_clf()

# reading test data from STDIN
N = int(raw_input())
for n in range(N):
    inp = raw_input()
    test_data.append(inp)

print test_data

model.predict(test_data)