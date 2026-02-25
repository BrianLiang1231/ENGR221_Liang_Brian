"""
Author: YOUR NAME
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""

from song import Song

class Playlist():
    # The constructor is run every time a new Playlist object is created
    # max_num_songs is the maximum number of songs you can have in the playlist
    def __init__(self, initial_songs):
        # Stores the songs in the playlist
        # It is initially a list of max_num_songs number of None objects
        self.songs = initial_songs
        # The current number of songs in the playlist
        self.num_songs = len(initial_songs)               
        # The maximum number of songs the playlist can have
        self.max_num_songs = len(initial_songs)
    ###########
    # Methods #
    ###########

    # Return the number of songs in the playlist
    def get_num_songs(self):
        return self.num_songs 
    
    # Return the current songs list
    def get_songs(self):
        return self.songs 
    
    # Return the song at index idx or
    # Return None if idx is outside of bounds
    def get_song_at_idx(self, idx):
        if 0 <= idx and idx < self.num_songs:
            return self.songs[idx]
    
    # Set index idx to the given song
    # Do not change anything if idx is outside of bounds
    def set_song_at_idx(self, idx, song):
        if 0 <= idx and idx < self.num_songs:
            self.songs[idx] = song 

    # Insert a song to the end of the playlist
    def insert_song(self, song):
        if self.num_songs == self.max_num_songs:
            #Increase capacity by 1
            capacity = 1 if self.max_num_songs == 0 else self.max_num_songs + 1
            #Create new list with increased capacity
            new_song = [None] * capacity
        # Copy existing songs
            for i in range(self.num_songs):
                new_song[i] = self.songs[i]
            #replace list
            self.songs = new_song
            self.max_num_songs = capacity
        #insert new song
        self.songs[self.num_songs] = song
        self.num_songs += 1

    # Return the index of the given song title in the playlist,
    # or return -1 if the song is not in the playlist
    def search_by_title(self, song_title):
        # Only search the indices with songs
        for i in range(self.num_songs):
            # Check the value at the current index 
            if self.songs[i].title == song_title:
                # Return the index
                return i 
            
        # If we got here, we did not find the song so return -1
        return -1
    
    # Delete the first occurrence of the song title in the playlist
    # Returns True if the song was deleted, or False if not
    def delete_by_title(self, song_title):
        delete_song = 0
        #find the song
        idx = self.search_by_title(song_title)
        #traversing list
        while idx != -1:
            #decrease size of list
            self.num_songs -= 1 
            #shift elements left
            for j in range(idx, self.num_songs):
                self.songs[j] = self.songs[j + 1]
            #increment counter
            delete_song += 1
            #search for more occurances
            idx = self.search_by_title(song_title)
        #return number of songs deleted
        return delete_song
    

    def traverse(self):
        for song in self.songs:
            print(song)

if __name__ == '__main__':
    # You can test your code here
    songs = [Song("Golden", "HUNTR/X"),
             Song("Ordinary", "Alex Warren"),
             Song("What I Want", "Morgan Wallen ft. Tate McRae"),
             Song("Your Idol", "Saja Boys"),
             Song("Soda Pop", "Saja Boys")]
    
    p = Playlist(3)