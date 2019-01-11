from urllib.request import urlopen
from bs4 import BeautifulSoup

MEMBERS = 'https://onlinesequencer.net/members'

def GetSequences(userID):
    '''
    Takes a user ID number as an argument.
    Returns a list of tuples containing IDs and titles of sequences.
    '''
    sequences = []
    page = 0
    while True:
        #Make and get data from the URL corresponding to the current page
        URL = f'{MEMBERS}/{userID}?start={page*72}'
        data = urlopen(URL).read().decode('UTF-8')

        #Parse HTML data
        html = BeautifulSoup(data, 'lxml')

        blocks = html.body.find_all("div", attrs={'class':'block'})

        #Get find the "Sequence" btitle in all blocks and get the one which didn't return None
        sequence_block, = [x for x in blocks if x.find("div", attrs={'class':'btitle'}, text = 'Sequences')]

        previews = sequence_block.find_all("div", attrs={'class':'preview'})

        #If there are no previews on this page, all songs have been found
        if not previews:
            return sequences

        for p in previews:
            #Grab every titls and ID, put in a list
            title = p.attrs['title']
            ID = p.find('a').attrs['href'][1:] #Find link and cut off the "/"
            sequences.append( (ID, title) )
            
        page += 1
