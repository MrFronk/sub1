import pandas as pd


# this method uses a pandas function that works pre-1.0.0 but wll break post 1.0.0
# See https://dev.pandas.io/docs/whatsnew/v1.0.0.html#backwards-incompatible-api-changes
def print_pandas():
    mi = pd.MultiIndex.from_product([[1, 2], ['a', 'b']], names=['x', 'y'])

    # This should display 'x':
    print(mi.levels[0].name)

    # Call upon a something that works pre-1.0.0:
    mi.levels[0].name = "new name"

    # This should display 'new name':
    print(mi.levels[0].name)
