from urllib.request import urlopen

MEMBERS = 'https://onlinesequencer.net/members'
def GetSequences(userID):
    '''
    Takes a user ID number as an argument.
    Returns a list of tuples containing IDs and titles of sequences.
    '''
    sequences = []
    URL = f'{MEMBERS}/{userID}'
    data = urlopen(URL).read().decode('UTF-8')

    #Find the Sequences box
    start = data.find('<div class="btitle">Sequences</div>')
    end = data.find('<div class="clear"></div>')
    data = data[start:end]

    #Find every instance of a song preview and gather their titles and IDs
    song_start = 0
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
        
    return sequences
    
##GetSequences(13889)
