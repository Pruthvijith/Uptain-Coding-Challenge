# Age Prediction Model from Email

## Description

This project aims to predict the age group of a user based on their email address. The prediction is made using several machine learning models, and the best model is selected based on the F1 score.

## Features Extraction

The model extracts several features from the email addresses to help predict the age group:

1. **Domain**: The domain part of the email (e.g., `gmail.com`).
2. **Birth Year**: Extracted from the email if present in the form of a 2 to 4-digit number.
3. **Age Group**: Categorized based on the birth year:
   - `young` for birth years between 1994 and 2006.
   - `medium` for birth years between 1974 and 1993.
   - `old` for birth years before 1974.
   - `unknown` if no valid birth year is found.
4. **Username Length**: Length of the username part of the email.
5. **Has Number**: Whether the username contains any digits.
6. **Has Special Character**: Whether the username contains any special characters.
7. **Old Domain**: Whether the domain is one of the older popular domains (`aol.com`, `hotmail.com`, `yahoo.com`).

## Model Training

The following models are used for training:

- Logistic Regression
- Random Forest Classifier
- Naive Bayes
- Support Vector Machine (SVM)

The training process includes:

1. **Data Preprocessing**: Features are extracted from the email addresses and one-hot encoding is applied to categorical variables.
2. **Label Encoding**: The age groups are encoded into numerical values.
3. **Imputation**: Missing values are imputed using the most frequent strategy.
4. **Train-Test Split**: The data is split into training and testing sets.
5. **Model Training**: Each model is trained, and the best model is selected based on the highest weighted F1 score.

## Running the Model

### Requirements

- Python 3.6 or higher
- Required libraries: `pandas`, `scikit-learn`

### Minimal System Requirements

- RAM: 4 GB
- CPU: Dual-core processor

### Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
