from urllib.request import urlopen
from webparser import GetSequences
import os
import sys


def IsInteger(x):
    try: int(x)
    except ValueError: return False
    else: return True
    
def DownloadSequence(filePath, ID):
    URL = f'https://onlinesequencer.net/app/midi.php?id={ID}'
    data = urlopen(URL).read()
    with open(filePath, 'wb') as f:
        f.write(data)

def main():
    if len(sys.argv) == 1:
        #Get userID through input if argument is not provided
        userID = input('User ID: ')
    elif len(sys.argv) == 2:
        #Get userID through argument if it was provided
        userID = sys.argv[1]
    else:
        print('USAGE: SequenceGrabber <User ID>')
        return
    
    #Ensure that the user ID is a number
    if not IsInteger(userID):
        print('User ID must be an integer.')

    userID = int(userID)

    #Create a folder for this user
    if not os.path.exists(str(userID)):
        os.makedirs(str(userID))

    #Download each sequence
    sequences = GetSequences(userID)
    for s in sequences:
        seqID, title = s
        fileName = ''.join(x for x in f'{seqID} - {title}.mid' if x not in '\/:*?<>|')
        filePath = f'{userID}\\{fileName}'
        if not os.path.isfile(filePath):
            print(f'Downloading {fileName}')
            DownloadSequence(filePath, seqID)
        

        
if __name__ == '__main__':
    main()
