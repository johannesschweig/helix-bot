import pandas as pd

# jokes
jokes = pd.read_csv('data/jokes.csv', sep=';', quotechar="'")
categories = jokes['category'].unique()

def get_joke(text):
    # Tell user a joke out of categories (if he/she knows them; otherwise just the bad ones) 
    text = text.lower()
    cat = 'flach'
    if text in categories:
      cat = text
    return jokes[jokes['category'] == cat].sample()['joke'].item()
