from urllib.request import urlopen

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

        #Find the Sequences box
        start = data.find('<div class="btitle">Sequences</div>')
        end = data.find('<div class="clear"></div>')
        data = data[start:end]

        #Stop looking if the page is empty. There are no more songs.
        if data.find('<div class="preview"') == -1:
            break
        
        #Find every instance of a song preview and gather their titles and IDs
        song_start = 0
        while True:
            song_start = data.find('<div class="preview"', song_start+1)

            #Stop when every song on this page has been found
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

