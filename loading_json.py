# sometimes we need to load up a JSON file
# this might contain configuration values

import json # this is built in to Python

def loadJSONfile():
    '''load a text file that contains JSON'''
    # open lets us work with file access objects. 'r' means read
    try:
        # the location of hte JSON file must bbe accessible
        # so a relative address or an absolute address
        with open('data/photos.json', 'r') as fin: 
            photos = json.load(fin) # also convert to Python structure
            return photos
            # we use 'with' because it will automatically close the file access obje t
    except Exception as err:
        print(f'oops {err}')

if __name__ == '__main__':
    r = loadJSONfile()
    print(r)