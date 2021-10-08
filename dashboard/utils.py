# preprocess data for dashboard

import pandas as pd


# TODO: get data from db, perform any joins/transforms/etc.


class Preprocess:
    def __init__(self):
        self.data = None

    def read_data(self) -> None:
        self.data = pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    def sample_data(self) -> None:
        self.data = pd.DataFrame({
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })
