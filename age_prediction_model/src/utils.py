import logging

def load_emails(file_path):
    try:
        with open(file_path, 'r') as file:
            emails = [line.strip() for line in file.readlines()]
        return emails
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return []
