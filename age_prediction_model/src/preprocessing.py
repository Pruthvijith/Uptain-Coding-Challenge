import pandas as pd

def preprocess_data(emails, label_encoder, imputer):
    df = pd.DataFrame({'email': emails})
    features = df['email'].apply(extract_features).apply(pd.Series)
    features = pd.get_dummies(features, columns=['domain'], drop_first=True)
    features['age_group'] = label_encoder.fit_transform(features['age_group'])
    columns = features.drop(columns=['age_group']).columns
    X = features.drop(columns=['age_group'])
    y = features['age_group']
    X_imputed = imputer.fit_transform(X)
    return X_imputed, y, columns

def align_features(features, columns):
    aligned_features = pd.DataFrame(features, columns=columns).reindex(columns=columns, fill_value=0)
    return aligned_features
