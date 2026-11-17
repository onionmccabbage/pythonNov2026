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
    # requests always returns a 'response' object
    # which includes any retrieved data (among other things)
    photos = response.json()
    return photos # this converts te JSON text to Python structure

if __name__ == '__main__':
    '''exercise this module'''
    r = getAllPhotos()
    # we now have a large Python structure
    # we may explore this structure
    print( r[5]['title'] )
    print(type(r))

