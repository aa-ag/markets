###--- IMPORTS ---###
import yfinance as yf


###--- GLOBAL VARIABLES ---###


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


###--- DRIVER CODE ---###
if __name__ == "__main__":
    company_level_info("MSFT")
