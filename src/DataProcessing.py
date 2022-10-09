import numpy as np
import pandas as pd


class DataProcessor():
    
    def __init__(self, path):
        self.path = path
    
    def load_data(self):
        self.data = pd.read_csv(self.path)
        return self
    
    def clean_data(self, self.data):
        df = self.data
        
        self.processed_data = (df
                               .assign(dteday = pd.to_datetime(df.dteday),
                                        time_label = lambda df_: pd.cut(df_.hr, bins = [-1,6,12,18,24], 
                                                                        labels = [1,2,3,4],ordered = True)
                                        )
                               )  
        return self