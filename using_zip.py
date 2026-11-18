# there is a feature built in to Python called zip
# it is nothing to do with compression or archives

channels = ['BBC1', 'BBC4', 'radio 4', 'radio 2']
main_topics = ['Wowser stuff', 'Artsy stuff', 'Newsy stuff', 'boomer_stuff']
other = ( 'Entertain', 'Educate' , 'Inform' )


c = zip(channels, main_topics) # , other)

for _ in c:
    print(_)