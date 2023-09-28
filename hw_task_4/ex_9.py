import numpy as np
import pandas as pd

class AI_Analysis:
    def __init__(self, path) -> None:
        self.path = path
        self.data = None

    def read_data(self):
        self.data = pd.read_csv(self.path)        
        print(self.data.head(10))

    def get_freq_review(self):        
        review_free_df = self.data[["Free/Paid/Other", "Review"]].dropna()
        review_free_df[pd.to_numeric(review_free_df['Review'], errors='coerce').notnull()]   
       # review_free_df["Review"] = review_free_df["Review"].astype(int)
        review_free_df = review_free_df.groupby(["Free/Paid/Other"]).sum() 
        print(review_free_df)

if __name__ == "__main__":  
    ai = AI_Analysis("hw_task_4\\all_ai_tool.csv")
    ai.read_data()
    print(ai.get_freq_review())
