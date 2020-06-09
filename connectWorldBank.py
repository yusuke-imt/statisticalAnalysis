from pandas_datareader import wb
import pandas as pd

def worldBank(countries, indicator):
    for index, country in enumerate(countries):
        df = wb.download(indicator=indicator, country=country, start=1960, end=2018)
        df = df.unstack(level=0)
        # 各国のdataframeをmerge
        if index == 0:
            dfs = df
        else:
            dfs[country] = df
    dfs.columns = countries
    return dfs
