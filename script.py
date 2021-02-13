###--- IMPORTS ---###
import yfinance as yf
import shutil


###--- GLOBAL VARIABLES ---###


###--- FUNCTIONS ---###
def company_level_info(company):
    '''
     Ticker module from yfinance provides
     company-level information.
    '''
    c = yf.Ticker(company)

    all_info = open('_.txt', 'w+')

    for k, v in c.info.items():
        all_info.write(f"{k}: {v}\n")

    all_info.close()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    company_level_info("MSFT")
