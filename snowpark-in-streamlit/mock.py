import pandas as pd
import numpy as np
from typing import Type, Union


def df(rows: int = 100, cols: Union[int, str] = 4):
    try:
        num_cols = len(cols)
    except TypeError:
        num_cols = cols
    return pd.DataFrame(np.random.randint(0, rows, size=(rows, cols)), columns=list('ABCD'))

    