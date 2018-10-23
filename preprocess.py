import pandas as pd
import numpy as np
import math
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sid = SentimentIntensityAnalyzer()

def read_data(filename):
    return pd.read_csv(filename, index_col=None).iloc[:,:].values

def group_by_product(reviews):
    productKeyToReviews = {}
    for review in reviews:
        if review[0] in productKeyToReviews:
            productKeyToReviews[review[0]].append([review[1:]])
        else:
            productKeyToReviews[review[0]] = []
            productKeyToReviews[review[0]].append([review[1:]])
    return productKeyToReviews

def convert_review_text_sentiment_score(productDict):
    sentiment_scores_reviews = {}
    for product, reviews in productDict.items():
        sum_pos_polarity, sum_ratings,sum_neg_polarity = 0.0, 0.0, 0.0
        count = 0
        for review in reviews:
            if isinstance(review[0][0], str):
                pos, neg = review_to_sentiment(review[0][0])
                sum_pos_polarity += pos
                sum_neg_polarity += neg
                sum_ratings += review[0][1]
                count += 1
        sentiment_scores_reviews[product] = (sum_polarity / count, sum_ratings / count)
    return sorted(sentiment_scores_reviews.items(), key=lambda value: (value[1][0] + value[1][1]) / 2)

def review_to_sentiment(review_text):
    polarities_pos = []
    polarities_neg = []
    
    lines_list = tokenize.sent_tokenize(review_text)
    for line in lines_list
        polarities_pos.append(sid.polarity_scores['pos'])
        polarities_neg.append(sid.polarity_scores['neg'])
        
    return np.mean(polarity_pos) , np.mean(polarity_neg)

print(convert_review_text_sentiment_score(group_by_product(read_data('./data/reviews_Clothing_Shoes_and_Jewelry_5.json.gz_combined.csv'))))
