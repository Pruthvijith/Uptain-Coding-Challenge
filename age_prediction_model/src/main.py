import logging
from src.model import AgePredictionModel
from src.utils import load_emails

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    model = AgePredictionModel()
    emails = load_emails('data/emails.txt')

    if not emails:
        return

    model.train_model(emails)

    test_emails = [
        "john.doe2003@gmail.com",
        "susan.smith1992@yahoo.com",
        "robert.williams1950@aol.com",
        "amy.jones@unknown.com"
    ]

    results = []
    for email in test_emails:
        try:
            prediction = model.get_prediction(email)
            results.append((email, prediction))
        except Exception as e:
            logging.error(f"Error predicting age for {email}: {e}")

    for email, result in results:
        logging.info(f"Email: {email}, Prediction: {result}")

    return results


if __name__ == "__main__":
    results = main()
