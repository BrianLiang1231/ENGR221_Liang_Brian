class NoDuplesPlaylist:
    
    def __init__(self, initial_songs):
        #list has length of initial songs
        self.songs = [None] * len(initial_songs)
        self.num_songs = 0
        #Prevent duplicates from being added
        for song in initial_songs:
            duplicate = False
            #search for duplicates
            for i in range(self.num_songs):
                #if song title and artist match there is a duplicate
                if (self.songs[i].title == song.title and self.songs[i].artist == song.artist):
                    #end loop if true
                    duplicate = True
                    break
            #add song and increment list
            if not duplicate:
                self.songs[self.num_songs] = song
                self.num_songs += 1
        #maximum number of songs is amount added initially
        self.max_num_songs = self.num_songs
    
    #Search songs by title returning 1 if found and -1 if not
    def search_by_title(self, song_title):
        #search for song title
        for i in range(self.num_songs):
            #checking value at current index
            if self.songs[i].title == song_title:
                #if found return 1
                return i
        #return -1 if not found
        return -1

    #insert song at the end
    def insert_song(self, song):
        #Prevent duplicates from being added
        for i in range(self.num_songs):
            if (self.songs[i].title == song.title and self.songs[i].artist == song.artist):
                return
        #if playlist is full increase size
        if self.num_songs == self.max_num_songs:
            #increase capacity by 1
            capacity = 1 if self.max_num_songs == 0 else self.max_num_songs + 1
            #create new list with new capacity
            new_songs = [None] * capacity
            #copy existing songs
            for i in range(self.num_songs):
                new_songs[i] = self.songs[i]
            #replace list 
            self.songs = new_songs
            self.max_num_songs = capacity
        #insert new song
        self.songs[self.num_songs] = song
        self.num_songs += 1

    #delete song by title
    def delete_by_title(self, song_title):
        #search list 
        for i in range(self.num_songs):
            #finding specified song title
            if self.songs[i].title == song_title:
                #shift elements left
                for j in range(i, self.num_songs - 1):
                    self.songs[j] = self.songs[j + 1]
                #decrement list
                self.num_songs -= 1
                #return true if song title found
                return True
        #return false if song title not found
        return False
    
    #print all songs in playlist
    def traverse(self):
        for i in range(self.num_songs):
            print(self.songs[i])
