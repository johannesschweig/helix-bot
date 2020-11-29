import pandas as pd

# jokes
jokes = pd.read_csv('data/jokes.csv', sep=';', quotechar='\'')
# categories
categories = jokes['category'].unique()
categories_cleaned = [x for x in categories]
categories_cleaned.append('flach')
categories_cleaned.insert(0, 'random')
categories_cleaned.remove('bedenklich')

def get_joke(text):
    # Tell user a joke out of categories (if he/she knows them; otherwise just the bad ones) 
    text = text.lower()
    if text in categories:
      return jokes[jokes['category'] == text].sample()['joke'].item().replace('#', '\n')
    else:
      return jokes.sample()['joke'].item().replace('#', '\n')
