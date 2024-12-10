from abc import ABC, abstractmethod
class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Artist(name={self.name!r})"

class Album:
    def __init__(self, title, release_year, artist):
        self.title = title
        self.release_year = release_year
        self.artist = artist
        self.songs = []
        artist.add_album(self)

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def __repr__(self):
        return f"Album(title={self.title!r}, artist={self.artist!r})"


class AbstractSong(ABC):
    @abstractmethod
    def get_details(self):
        pass


class Song(AbstractSong):
    def __init__(self, title, duration, album):
        self.title = title
        self.duration = duration
        self.album = album

    def get_details(self):
        return f"{self.title} - {self.album.artist.name} [{self.duration} mins] from {self.album}"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Song(title={self.title!r}, duration={self.duration!r})"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        user.playlists.append(self)
    def __len__(self):
        return len(self.songs)

    def add_song(self, song):
        song.position = len(self.songs) + 1
        self.songs.append(song)

    def __repr__(self):
        return f"Playlist(name={self.name!r}, number of songs={len(self.songs)})"

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            for index, song in enumerate(self.songs):
                song.position = index + 1
            print(f"'{song.title}' removed from playlist '{self.name}'.")
        else:
            print(f"'{song.title}' not found in playlist '{self.name}'.")

    def show_playlist(self):
        if not self.songs:
            print(f"Playlist '{self.name}' is empty.")
        else:
            print(f"Songs in playlist '{self.name}':")
            for song in self.songs:
                print(f" - {song.get_details()}")

    def __str__(self):
        return self.name

class AbstractSubscription(ABC):
    @abstractmethod
    def show_info(self):
        pass


class Subscription(AbstractSubscription):
    def __init__(self, plan_name, price, benefits, can_skip_ads=None, can_skip_songs=None):
        self.plan_name = plan_name
        self.price = price
        self.benefits = benefits
        self.can_skip_ads = can_skip_ads
        self.can_skip_songs = can_skip_songs

    def show_info(self):
        print(f"Plan Name: {self.plan_name}, Price: {self.price}, Benefits: {self.benefits}")


class FreeSubscription(Subscription):
    def __init__(self):
        super().__init__("Free", 0, ["Limited access", "Ads included"])


class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__("Premium", 9.99, ["No ads", "Offline playback", "High-quality audio"])


class User(ABC):
    users = []

    def __init__(self, username, password, subscription=None):
        self.username = username
        self._password = password
        self.playlists = []
        self.subscription = subscription
        User.users.append(self)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if new_password:
            self._password = new_password
        else:
            print("Password shouldn't be empty")

    @classmethod
    def login(cls, username, password):
        for user in cls.users:
            if user.username == username and user._password == password:
                print(f"User {username} logged in.")
                return user
        print("Check username or password.")
        return None

    @classmethod
    def signin(cls, username, password, subscription=None):
        for user in cls.users:
            if user.username == username:
                print(f"{username} already exists.")
                return None
        new_user = ConcreteUser(username, password, subscription)
        print(f"User {username} signed in with subscription: {subscription.plan_name}.")
        return new_user

    def create_playlist(self, name):
        new_playlist = Playlist(name)
        self.playlists.append(new_playlist)
        print(f"Playlist '{name}' created for user '{self.username}'.")
        return new_playlist

    def show_playlists(self):
        print(f"User '{self.username}' Playlists:")
        for playlist in self.playlists:
            print(f"- {playlist.name}")

    @abstractmethod
    def play_song(self, song):
        pass


class ConcreteUser(User):
    def play_song(self, song):
        if self.subscription and self.subscription.can_skip_ads:
            print(f"{song.title} is playing without ads...")
        else:
            print(f"{song.title} is currently playing")


songs = []
artists = []

artist1 = Artist("Artist 1")
album1 = Album("Album 1", 2023, artist1)
song1 = Song("song 1", 3.5, album1)
song2 = Song("song 2", 4.0, album1)
album1.add_song(song1)
album1.add_song(song2)
artists.append(artist1)
songs.extend([song1, song2])

artist2 = Artist("Artist 2")
album2 = Album("Album 2", 2024, artist2)
song3 = Song("song 3", 4.5, album2)
album2.add_song(song3)
artists.append(artist2)
songs.append(song3)
def main_menu():
    while True:
        print("1/ sign in")
        print("2/ log in")
        print("3/ exit")
        choice = input("choose an option(1,2 or 3): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            plan = input("Choose subscription (free/premium): ")

            if plan.lower() == "free":
                subscription = FreeSubscription()
            elif plan.lower() == "premium":
                subscription = PremiumSubscription()
            else:
                print("Invalid subscription choice.")
                continue

            ConcreteUser.signin(username, password, subscription)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User.login(username, password)
            if user:
                user_menu(user)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

def user_menu(user):
    while True:
        print("1/ create playlist")
        print("2/ show playlists")
        print("3/ add song to playlist")
        print("4/ play song")
        print("5/ subscription status")
        print("6/ change password")
        print("7/ Show Artists")
        print("8/ show songs in playlist")
        print("9/ show All songs in library")
        print("10/ log out")
        choice = input("choose: ")

        if choice == "1":
            playlist_name = input("enter playlist name: ")
            user.create_playlist(playlist_name)

        elif choice == "2":
            user.show_playlists()

        elif choice == "3":
            playlist_name = input("Enter the playlist name: ")
            song_title = input("Enter the song title: ")
            selected_playlist = None
            for playlist in user.playlists:
                if playlist.name == playlist_name:
                    selected_playlist = playlist
                    break
            if selected_playlist:
                new_song = Song(song_title, duration=None, album=None)
                selected_playlist.add_song(new_song)
                print(f"'{song_title}' has been added to playlist '{selected_playlist.name}'.")
            else:
                print(f"Playlist '{playlist_name}' not found. Please check the name and try again.")

        elif choice == "4":
            song_title = input("enter song to play: ")
            for playlist in user.playlists:
                for song in playlist.songs:
                    if song.title == song_title:
                        user.play_song(song)
                        break
                break
            else:
                print("Song not found in any playlist.")

        elif choice == "5":
            if user.subscription:
                print(f"plan: {user.subscription.plan_name}")
        elif choice == "6":
            new_password = input("enter new password: ")
            user.password = new_password
            print(f"{user.password} is the new password")


        elif choice == "7":
            print("\nArtists:")
            for artist in artists:
                print(f" - {artist.name}")


        elif choice == "8":
            playlist_name = input("Enter playlist name to view songs: ")
            for playlist in user.playlists:
                if playlist.name == playlist_name:
                    playlist.show_playlist()
                    break
            else:
                print(f"Playlist '{playlist_name}' not found.")

        elif choice == "9":
            print("\nall Songs in Library:")
            for song in songs:
                print(f" - {song.get_details()}")

        elif choice == "10":
            print(f"goodbye, {user.username}")
            break
main_menu()