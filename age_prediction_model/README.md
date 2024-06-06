# Age Prediction Model from Email

## Description

This project aims to predict the age group of a user based on their email address using machine learning models. By extracting specific features from email addresses, the model can classify users into different age groups: young, medium, old, or unknown. The best-performing model is selected based on the F1 score during the training process.

## Methodology

### Feature Extraction

The model extracts several features from the email addresses to help predict the age group:

1. **Domain**: Extracts the domain part of the email (e.g., `gmail.com`).
2. **Birth Year**: Extracts a 2 to 4-digit number from the email, which may represent the birth year.
3. **Age Group**: Categorizes based on the extracted birth year:
   - `young` for birth years between 1994 and 2006.
   - `medium` for birth years between 1974 and 1993.
   - `old` for birth years before 1974.
   - `unknown` if no valid birth year is found.
4. **Username Length**: Measures the length of the username part of the email.
5. **Has Number**: Checks if the username contains any digits.
6. **Has Special Character**: Checks if the username contains any special characters.
7. **Old Domain**: Identifies if the domain is one of the older popular domains (`aol.com`, `hotmail.com`, `yahoo.com`).

### Model Training Process

The training process includes the following steps:

1. **Data Preprocessing**: 
   - Extracts features from the email addresses.
   - Applies one-hot encoding to categorical variables (e.g., domain).
   - Encodes age groups into numerical values using `LabelEncoder`.
   - Imputes missing values using the most frequent strategy.

2. **Train-Test Split**: Splits the data into training and testing sets (80% training, 20% testing).

3. **Model Training**: Trains the following machine learning models:
   - Logistic Regression
   - Random Forest Classifier
   - Naive Bayes
   - Support Vector Machine (SVM)

4. **Model Evaluation**: Evaluates each model using the F1 score and selects the best-performing model.

### Running the Model

#### Requirements

- Python 3.7 or higher
- Required libraries: `pandas`, `scikit-learn`

#### Minimal System Requirements

- RAM: 4 GB
- CPU: Dual-core processor

#### Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   
2. Install the required Python packages:
   pip install -r requirements.txt

3. Run the main script:
   python src/main.py

The model will train on the provided email data and test on predefined test emails provided in main function.
The output will be logged to the console, showing the email and the predicted age group along with the confidence scores.

### Example
#### Navigate to the project directory
cd age_prediction_model

#### Install dependencies
pip install -r requirements.txt

#### Run the model
python src/main.py

