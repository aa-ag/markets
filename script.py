###--- IMPORTS ---###
import yfinance as yf


###--- GLOBAL VARIABLES ---###

###--- FUNCTIONS ---###
m = yf.Ticker("MSFT")

print(m.info)

###--- DRIVER CODE ---###
if __name__ == "__main__":
    pass
