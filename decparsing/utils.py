import re

import pandas as pd
import numpy as np


def is_url(path_or_url: str) -> bool:
    # from https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, path_or_url) is not None


def handle_duplicates(names):
    names_series = pd.Series(names)
    counts = names_series.value_counts()
    for n in counts.index.values[counts>1]:
        e = 1
        for i in np.where(names_series==n)[0][1:]:
            new_name = f"{n};;{e}"
            names_series.iloc[i] = new_name
            e += 1
    return names_series.tolist()
