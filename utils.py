import pandas as pd

# jokes
jokes = pd.read_csv('data/jokes.csv', sep=';', quotechar='\'')
# categories
categories = jokes['category'].unique()
categories_cleaned = [x for x in categories]
categories_cleaned.remove('flach')
categories_cleaned.remove('bedenklich')

def get_joke(text):
    # Tell user a joke out of categories (if he/she knows them; otherwise just the bad ones) 
    text = text.lower()
    cat = 'flach'
    if text in categories:
      cat = text
    return jokes[jokes['category'] == cat].sample()['joke'].item().replace('#', '\n')
