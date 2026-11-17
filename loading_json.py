# sometimes we need to load up a JSON file
# this might contain configuration values

import json # this is built in to Python

def loadJSONfile():
    '''load a text file that contains JSON'''
    # open lets us work with file access objects. 'r' means read
    try:
        with open('photos.json', 'r') as fin: 
            photos = json.load(fin)
            return photos
            # we use 'with' because it will automatically close the file access obje t
    except Exception as err:
        print(f'oops {err}')

