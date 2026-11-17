# we can grab public data from internet API sources
import requests

# an API is an Application Programming Interface
# REST (RESTful) REpresent STate
# Often data is presented as JSON (Javascript Object Notation)

def getAllPhotos():
    '''grab all the data from a REST API for photos'''
    api_url = 'http://jsonplaceholder.typicode.com/photos'
    photos = [] # we have an empty list to start with
    # whenever we interact with stuff outside of Python
    # there is a chance things might go wrong
    try:
        response = requests.get(api_url)
        # requests always returns a 'response' object
        # which includes any retrieved data (among other things)
        photos = response.json()
        return photos # this converts te JSON text to Python structure
    except Exception as err: # if anything goes wrong, we run this block
        print(f'Something went wrong: {err}')

def getOnePhoto(id=1): # set a sensible default
    '''use an id to get only one matching photo'''
    # we would usually validate that id is indeed an acceptable value
    try:
        photo = requests.get(f'http://jsonplaceholder.typicode.com/photos/{id}')
        return photo.json()
    except Exception as err:
        print(f'Something went wrong: {err}')

if __name__ == '__main__':
    '''exercise this module'''
    r = getAllPhotos()
    # we now have a large Python structure
    # we may explore this structure
    print( r[5]['title'] )
    print(type(r))
    # use our single-photo getter
    s = getOnePhoto(42)
    print(s)

