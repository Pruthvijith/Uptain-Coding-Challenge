import re

def extract_features(email):
    features = {}
    domain = email.split('@')[-1]
    features['domain'] = domain
    match = re.search(r'\d{2,4}', email)
    if match and 0 < len(email.split('@')[0]) <= 15:
        number = int(match.group(0))
        if 1994 <= number <= 2006:
            features['birth_year'] = number
            features['age_group'] = 'young'
        elif 1974 <= number < 1994:
            features['birth_year'] = number
            features['age_group'] = 'medium'
        elif number < 1974:
            features['birth_year'] = number
            features['age_group'] = 'old'
        else:
            features['age_group'] = 'unknown'
    else:
        features['age_group'] = 'unknown'

    username = email.split('@')[0]
    features['username_length'] = len(username)
    features['has_number'] = any(char.isdigit() for char in username)
    features['has_special_char'] = any(not char.isalnum() for char in username)
    old_domains = {'aol.com', 'hotmail.com', 'yahoo.com'}
    features['old_domain'] = 1 if domain in old_domains else 0
    return features
