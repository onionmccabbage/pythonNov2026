# we can grab public data from internet API sources
import requests

# an API is an Application Programming Interface
# REST (RESTful) REpresent STate
# Often data is presented as JSON (Javascript Object Notation)

def getAllPhotos():
    '''grab all the data from a REST API for photos'''
    api_url = 'http://jsonplaceholder.typicode.com/photos'
    photos = [] # we have an empty list to start with
    response = requests.get(api_url)
    return response.json()

if __name__ == '__name__':
    '''exercise this module'''
    r = getAllPhotos()
    print(r)

