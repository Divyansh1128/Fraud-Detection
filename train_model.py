from fraud_detection import LogisticRegression, load_data, preprocess_data, split_data
import joblib

def train_and_save_model():
    # Load and preprocess data
    X, y = load_data('credit_card_transactions.csv')
    X = preprocess_data(X)
    
    # Split data
    X_train, _, y_train, _ = split_data(X, y)
    
    # Train model
    model = LogisticRegression(learning_rate=0.01, num_iterations=1000)
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, 'fraud_model.joblib')

if __name__ == "__main__":
    train_and_save_model()