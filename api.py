import currencyapicom
client = currencyapicom.Client('cur_live_4j1xBcRfJNWonY5G6wHzenMRZKFBzqyY4oS1XlYW')
def convertCurrencies(c1: str, c2: str):
    result = client.latest(c1, [c2])
    value = result['data'][c2]['value']
    #print(result)
    return value