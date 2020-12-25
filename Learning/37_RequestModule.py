'''
    #Summary

Usage:
      This useful for sending HTTP request to the browser within the code

Things:
      1. get(api link) => This will save the api link and return it's content
      2. post() => This has an API end point and some data

Status Quotes:
      https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

'''
import requests

# @ Defining

# * This will get the api dict from the link and then store it into a variable
try:
    API = requests.get(
        'https: // financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo')


# * This is the use of post()

# ! Here I am make the end point this is URL
url1 = 'www.google.com'
# ! This is the data we want to send
data = {
    'Point 1':  8,
    'Point 2': 19,
}

# ? Afer we assign the url with the data we get a status quote this will tell what has happen
response = requests.post(url=url1, data=data)


# ? Execution
if __name__ == '__main__':
    print(API.text)
    print('--------------------------------------------------------------------------------')

    print(f'Status code is {response}')
