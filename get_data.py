
import yfinance as yf
import pandas as pd

def get_tickers():
    # Download the list of S&P 500 companies from Wikipedia
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    sp500_df = table[0]
    
    # # Filter the DataFrame for rows where the GICS Sector is Information Technology
    # tech_df = sp500_df[(sp500_df['GICS Sector'] == 'Information Technology') | (sp500_df['GICS Sector'] == 'Financials')]
    
    # Extract the tickers
    tickers = sp500_df['Symbol'].tolist()
    return tickers

def get_price(tickers, start_date, end_date):
    """
    Download the daily prices for the given tickers and date range.

    Parameters:
    tickers (list): A list of ticker symbols.
    start_date (str): The start date in the format 'YYYY-MM-DD'.
    end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
    pandas.DataFrame: A DataFrame containing the daily prices for the given tickers and date range.
    """
    # Download the daily prices for the given tickers and date range
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

def get_earnings_transcripts(file_path, tickers):
    """
    Download data from Kaggle, save it to file_path and filter it for the given tickers.
    https://www.kaggle.com/datasets/tpotterer/motley-fool-scraped-earnings-call-transcripts
    """
    # Load the earnings transcript data
    data = pd.read_pickle(file_path)
    
    # Filter the data for the given tickers
    filtered_data = data[data['ticker'].isin(tickers)]
    
    return filtered_data

