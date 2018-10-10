# Used to get rid of unnecessary data in the csv files
import os
import pandas as pd
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

if __name__ == "__main__":

    ratings_dir = './data/ratings/'
    reviews_dir = './data/reviews/'
    
    files = [(root,file) for (root, dirs, files) in os.walk(reviews_dir) for file in files if file.endswith('.gz')]
 
    for directory, file_name in files:
            
        # rating_source = ratings_dir + 'ratings_' + file_name + '.csv'
        # rating_data = pd.read_csv(rating_source,header=None,index_col=None).iloc[:,:].values
    
        review_data = getDF(directory + file_name).iloc[:,[1,4,5,6]]
        
        review_data.to_csv(path_or_buf='./data/' + file_name + '_combined.csv',
                            header=['item_id','review','rating','review_summary'], index=False)
        
        
            

