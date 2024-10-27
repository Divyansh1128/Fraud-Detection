import csv
import math
import random

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def fit(self, X, y):
        num_samples, num_features = len(X), len(X[0])
        self.weights = [0] * num_features
        self.bias = 0

        for _ in range(self.num_iterations):
            for i in range(num_samples):
                linear_model = sum(self.weights[j] * X[i][j] for j in range(num_features)) + self.bias
                y_predicted = self.sigmoid(linear_model)

                for j in range(num_features):
                    self.weights[j] -= self.learning_rate * (y_predicted - y[i]) * X[i][j]
                self.bias -= self.learning_rate * (y_predicted - y[i])

    def predict(self, X):
        linear_model = sum(self.weights[j] * X[j] for j in range(len(X))) + self.bias
        y_predicted = self.sigmoid(linear_model)
        return 1 if y_predicted > 0.5 else 0

def load_data(filename):
    X, y = [], []
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            X.append([float(x) for x in row[:-1]])
            y.append(int(row[-1]))
    return X, y

def preprocess_data(X):
    # Normalize features
    num_features = len(X[0])
    min_values = [min(X[i][j] for i in range(len(X))) for j in range(num_features)]
    max_values = [max(X[i][j] for i in range(len(X))) for j in range(num_features)]
    
    for i in range(len(X)):
        for j in range(num_features):
            if max_values[j] - min_values[j] != 0:
                X[i][j] = (X[i][j] - min_values[j]) / (max_values[j] - min_values[j])
            else:
                X[i][j] = 0
    return X

def split_data(X, y, test_size=0.2):
    combined = list(zip(X, y))
    random.shuffle(combined)
    X[:], y[:] = zip(*combined)
    split_index = int(len(X) * (1 - test_size))
    return X[:split_index], X[split_index:], y[:split_index], y[split_index:]

def evaluate_model(y_true, y_pred):
    tp, tn, fp, fn = 0, 0, 0, 0
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            tp += 1
        elif true == 0 and pred == 0:
            tn += 1
        elif true == 0 and pred == 1:
            fp += 1
        else:
            fn += 1
    
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return accuracy, precision, recall, f1_score

def main():
    # Load and preprocess data
    X, y = load_data('credit_card_transactions.csv')
    X = preprocess_data(X)
    
    # Split data
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train model
    model = LogisticRegression(learning_rate=0.01, num_iterations=1000)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = [model.predict(x) for x in X_test]
    accuracy, precision, recall, f1_score = evaluate_model(y_test, y_pred)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1_score:.4f}")

if __name__ == "__main__":
    main()