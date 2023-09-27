import numpy as np
import datetime
import pandas as pd

class Analysis:
    def __init__(self, path) -> None:
        self.path = path
        self.data = None

    def read_data(self):
        self.data = pd.read_csv(self.path, sep=',', usecols=(0,3))##np.genfromtxt(self.path, delimiter=',', names=True, usecols=(0,3))#
        print(self.data.head(5))

    def get_country(self):
        return self.data["country"].value_counts().nlargest(1)

    def get_month(self):
        temp_df = pd.DataFrame()
        self.data['datetime'] = pd.to_datetime(self.data['datetime'], errors='coerce')
        temp_df["month"] = self.data["datetime"].dt.month
        return temp_df["month"].value_counts().nlargest(1)


if __name__ == "__main__":
    anaysis = Analysis("hw_task_4\\nlo.csv")
    anaysis.read_data()
    print(anaysis.get_country())
    print(anaysis.get_month())