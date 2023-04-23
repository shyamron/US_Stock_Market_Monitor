from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import pandas as pd
dow_list = si.tickers_dow()



dow_stats = {}
for ticker in dow_list:
    temp = si.get_stats_valuation(ticker)
    temp = temp.iloc[:,:2]
    temp.columns = ["Attribute", "Recent"]
    dow_stats[ticker] = temp

combined_stats = pd.concat(dow_stats)
combined_stats = combined_stats.reset_index()

del combined_stats["level_1"]
# update column names
combined_stats.columns = ["Ticker", "Attribute", "Recent"]
print(combined_stats)
