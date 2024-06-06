import logging
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from src.feature_extraction import extract_features
from src.preprocessing import preprocess_data, align_features


class AgePredictionModel:
    def __init__(self):
        self.models = {
            "logistic_regression": LogisticRegression(max_iter=1000),
            "random_forest": RandomForestClassifier(),
            "naive_bayes": GaussianNB(),
            "svm": SVC(probability=True)
        }
        self.best_model = None
        self.le = LabelEncoder()
        self.imputer = SimpleImputer(strategy='most_frequent')
        self.columns = None

    def train_model(self, emails):
        X, y = preprocess_data(emails, self.le, self.imputer)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        best_f1 = 0
        for model_name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            f1 = f1_score(y_test, y_pred, average='weighted')
            logging.info(f"{model_name} F1 score: {f1}")
            if f1 > best_f1:
                best_f1 = f1
                self.best_model = model

    def get_prediction(self, email):
        if not self.best_model:
            raise Exception("Model is not trained yet.")
        df = pd.DataFrame({'email': [email]})
        features = df['email'].apply(extract_features).apply(pd.Series)
        email_features = pd.get_dummies(features, columns=['domain'], drop_first=True)
        email_features_aligned = align_features(email_features, self.columns)
        email_features_imputed = self.imputer.transform(email_features_aligned)
        prediction = self.best_model.predict(email_features_imputed)[0]
        score = max(self.best_model.predict_proba(email_features_imputed)[0])

        if score < 0.6:
            prediction = "unsure"
            score = 0.0
        else:
            prediction = self.le.inverse_transform([prediction])[0]
            score = score.item()

        return {"age": prediction, "score": score}
