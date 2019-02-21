from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

digits = load_digits();

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.33, random_state=3)

clf = DecisionTreeClassifier(criterion='gini')
clf = clf.fit(X_train, y_train)

test_predict = clf.predict(X_test)
score = accuracy_score(y_test, test_predict)
print("CART 分类树准确率 %.4lf" % score)