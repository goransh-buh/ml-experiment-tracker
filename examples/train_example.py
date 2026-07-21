"""
Example: using the tracker while training a simple scikit-learn model.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from tracker.run import Run

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

run = Run("iris_logistic_regression")
run.log_param("model", "LogisticRegression")
run.log_param("test_size", 0.2)
run.log_param("random_state", 42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

run.log_metric("accuracy", acc)
run.finish()

print(f"Run complete. Accuracy: {acc:.4f}")
print(f"Logged to: {run.log_dir}")
