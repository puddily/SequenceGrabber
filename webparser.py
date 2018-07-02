from urllib.request import urlopen

MEMBERS = 'https://onlinesequencer.net/members'
def GetSequences(userID):
    '''
    Takes a user ID number as an argument.
    Returns a list of tuples containing IDs and titles of sequences.
    '''
    sequences = []
    page = 0;
    
    while True:
        #Find the Sequences box
        pageNumber = f'?start={page*72}'
        URL = f'{MEMBERS}/{userID}{pageNumber}'
        data = urlopen(URL).read().decode('UTF-8')

        start = data.find('<div class="btitle">Sequences</div>')
        end = data.find('<div class="clear"></div>')
        data = data[start:end]

        #Find every instance of a song preview and gather their titles and IDs
        song_start = 0
        song_start = data.find('<div class="preview"', song_start+1)
        if song_start == -1:
            break
        while True:
            song_start = data.find('<div class="preview"', song_start+1)
            if song_start == -1:
                break
            title_start = data.find('title="', song_start) + len('title="')
            title_end = data.find('">\n', title_start)
            title = data[title_start:title_end]

            ID_start = data.find('<a href="/', title_end) + len('<a href="/')
            ID_end = data.find('"', ID_start)
            ID = int(data[ID_start:ID_end])
            sequences.append( (ID, title) )
        page += 1
        
    return sequences
    
##GetSequences(13889)
