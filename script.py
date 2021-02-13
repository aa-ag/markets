###--- IMPORTS ---###
import yfinance as yf


###--- FUNCTIONS ---###
def company_level_info(company):
    '''
     Ticker module from yfinance provides
     company-level information.
    '''

    c = yf.Ticker(company)

    company_info = c.info

    company_name = company_info['shortName'].split()[0]

    all_info = open(f'{company_name.lower()}.txt', 'w+')

    all_info.write(f"*** {company_name.upper()} ***\n\n")

    for i, (k, v) in enumerate(company_info.items()):
        all_info.write(f"{i+1}. {k}: {v}\n")

    all_info.close()


def shareholder_info(company):
    '''
     modules:
     major_holders, institutional_holders, balance_sheet, recommendations
    '''
    c = yf.Ticker(company)

    print(c.major_holders)
    print(c.institutional_holders)
    print(c.balance_sheet)
    print(c.calendar)


def multiple_tickers():
    tickers = yf.Tickers('msft aapl goog')

    company_info = tickers.tickers.AAPL.info
    print(company_info)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    # company_level_info("MSFT")
    # shareholder_info("MSFT")
    multiple_tickers()
