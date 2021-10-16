from queue import Queue
import random

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
 
class Queue:
    def __init__(self, current_song_index=0, currently_playing=False):
        self.items = []
        self.set_current_song_index(current_song_index)
        self.set_currently_playing(currently_playing)

    def set_current_song_index(self, index):
        self.current_song_index = index

    def set_currently_playing(self, currently_playing):
        self.curently_playing = currently_playing

    def add_song(self, song):
        if self.size() > 0:
            self.items.insert(self.size() + 1, song)
        else:
            self.items.insert(0, song)

    def size(self):
        return len(self.items)

    def play(self, song_index):
        self.current_song_index = song_index
        
        self.set_currently_playing(True)
        
        print("\nPlaying....")

        print(self.items[self.current_song_index])

    def show_play_list(self):
        num = 1

        print("\nSong List:\n")

        for item in self.items:
            print(str(num) + '. ' + str(item))
            num += 1

    def show_current_song(self):
        if self.curently_playing:
            print("\nCurrently Playing:")

            print(self.items[self.current_song_index])
        else:
            print('\nNothing is Playing!')

    def next(self):
        if self.curently_playing:
            playlist_length = len(self.items) - 1

            if self.current_song_index == playlist_length:
                next_song = 0
            else:
                next_song = self.current_song_index + 1

            print("\nSkipping....")

            self.play(next_song)
        else:
            print('\nNothing is Playing!')

    def prev(self):
        if self.curently_playing:
            playlist_length = len(self.items) - 1
            
            if self.current_song_index == 0:
                prev_song = playlist_length
            else:
                prev_song = self.current_song_index - 1

            print("\nReplaying....")
            
            self.play(prev_song)
        else:
            print('\nNothing is Playing!')

    def removeSong(self, title):
        song_index = 0

        for item in self.items:
            if item.title == title:
                self.items.pop(song_index)
                break   
            song_index += 1

    def shuffle(self):
        list_length = self.size()
        
        for i in range(list_length):
            # first element
            first_number = self.items.pop(0)
            self.items.append(first_number)
            
            # generate a random number 
            random_num = random.randint(0, list_length - 1)

            # random element 
            list_element = self.items.pop(random_num)
            self.items.append(list_element)
# Menu
def menu():
    print('\n')
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
    print('\n')

myMediaPlayer = Queue()

# Default Playlist
myMediaPlayer.add_song(Song('Essence', 'Wizkid'))
myMediaPlayer.add_song(Song('Cupid', '112'))
myMediaPlayer.add_song(Song('Wild Side', 'Normani, Cardi B'))
myMediaPlayer.add_song(Song('Outside', 'Meek Mill'))
myMediaPlayer.add_song(Song('Gyalis', 'Capella Grey'))
myMediaPlayer.add_song(Song('Love All', 'Drake, Jay-z'))
myMediaPlayer.add_song(Song('Damage', 'H.E.R'))
myMediaPlayer.add_song(Song('No Guidance', 'Chris Brown'))
myMediaPlayer.add_song(Song('Moon', 'Kanye West'))
myMediaPlayer.add_song(Song('Good Days', 'SZA'))


# Media Player
#region
while True:
    menu()
    choice = int(input())

    if choice == 1:
        # input Songs Title and Artist Name
        artist = input('Enter the Song Artist: ')
        title = input('Enter Song Title: ')

        # Add song to the playlist
        song = Song(title=title, artist=artist)
        myMediaPlayer.add_song(song)
        
        print("New Song: " + song.title + " Added to Playlist")
        
    elif choice == 2:
        # enter for Song Title 
        title = input('Enter the Song Title to be Removed: ')
        
        # Remove song input from playlist
        myMediaPlayer.removeSong(title)
        
        print("Song: " + title + " Removed from Playlist")

    elif choice == 3:
        # Play the playlist & Display song name is playing
        myMediaPlayer.play(0)
        
    elif choice == 4:
        # Skip to the next song on the playlist
        myMediaPlayer.next()
        
    elif choice == 5:
        # Go back to previous song

        myMediaPlayer.prev()

    elif choice == 6:
        # shuffle the playlist and play the first song

        myMediaPlayer.shuffle()

        print("Shuffling....")

        myMediaPlayer.show_play_list()

        myMediaPlayer.play(0)

    elif choice == 7:
        # show the song name and artist of the currently playing song
        myMediaPlayer.show_current_song()

    elif choice == 8:
        # display the current song list order
        myMediaPlayer.show_play_list()

    elif choice == 0:

        print("Goodbye.")
        break
#endregion