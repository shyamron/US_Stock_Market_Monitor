from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import pandas as pd
# tickers = yf.Tickers('*')
# print(len(tickers))
dow_list = si.tickers_dow()
# print("Tickers in Dow Jones:", len(dow_list))
# df=pd.DataFrame(dow_list)
# df.to_csv("dow_list.csv", index=False)

# def data(ticker,time):
#     ticker_list = ["amzn", "aapl", "ba"]
#     historical_datas = {}
#     for ticker in ticker_list:
#         historical_datas[ticker] = get_data(ticker)
    
#     print(historical_datas)
#     # if time=="Every Day":
#     #     time="1d"
#     # elif time=="Every Week":
#     #     time="1w"
#     # else:
#     #     time="1mo"
#     # get_data(ticker, start_date = None, end_date = None, index_as_date = True, interval = time)

#     # print(get_data)

# data("amnz",'12')


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
