import pandas as pd

# jokes
jokes = pd.read_csv('data/jokes.csv', sep=';', quotechar='\'')
# categories
categories = jokes['category'].unique()
categories_cleaned = [x for x in categories]
categories_cleaned.insert(0, 'random')
## hidden categories
categories_cleaned.remove('bedenklich')
categories_cleaned.remove('flach')

def get_joke(text):
    text = text.lower()
    # Tell user a joke out of categories (includes hidden categories)
    if text in categories:
      j = jokes[jokes['category'] == text]
    else: # Tell a random joke except 'bedenklich'
      j = jokes[jokes['category'] != 'bedenklich']
    return j.sample()['joke'].item().replace('#', '\n')
