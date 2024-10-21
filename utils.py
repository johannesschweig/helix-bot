import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()
API_KEY = os.getenv('API_KEY')
SHEET_NAME = 'jokes'
SHEET_ID = os.getenv('SHEET_ID')

def get_google_sheet_data(spreadsheet_id,sheet_name, api_key):
    # Construct the URL for the Google Sheets API
    url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{sheet_name}!A1:Z?alt=json&key={api_key}'

    try:
        # Make a GET request to retrieve data from the Google Sheets API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return None

# jokes
jokes = get_google_sheet_data(SHEET_ID, SHEET_NAME, API_KEY)
if not jokes:
    print("Failed to fetch data from Google Sheets API.")
## remove header row
jokes = jokes['values'][1:]
# categories
categories = list(set([x[0] for x in jokes]))
categories_cleaned = [c for c in categories]
categories_cleaned.insert(0, 'random')
## hidden categories
categories_cleaned.remove('bedenklich')
categories_cleaned.remove('flach')

def get_joke(text):
    text = text.lower()
    # Tell user a joke out of categories (includes hidden categories)
    if text in categories:
      matching_jokes = [ joke for joke in jokes if joke[0] == text ]
    else: # Tell a random joke except 'bedenklich'
      matching_jokes = [ joke for joke in jokes if joke[0] != 'bedenklich' ]
    return "\n".join(random.choice(matching_jokes)[1:])
    
#print(get_joke('flach'))
#print(get_joke('deine mutter'))