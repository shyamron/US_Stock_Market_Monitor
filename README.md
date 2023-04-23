# US_Stock_Market_Monitor

Monitor your Stocks

This is a web application that allows users to receive notification when the price of a given stock reaches a certain threshold.


TOOLS/ TECHNOLOGIES USED:
1. Python with Flask framework
2. HTML/CSS
3. Yahoo Finance API


Stock price data is retrieved from here--https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC
Files:
1. get_ticker.py is used to extract stock ticker symbols. Output is dow_list.csv
2. main.html has frontpage UI and backend.py uses Flask framework. Run "flask --app backend run" 
3. backend.py calls monitor function which is in checking_threshold.py. checking_threshold.py contains all functions that extracts live stock price, compares with threshold price and sends notifications

For futher details, see documentation-- https://drive.google.com/file/d/1NhP3Bs2A2ruhEBwBE3qIiHMVDyhQP4rG/view?usp=share_link
