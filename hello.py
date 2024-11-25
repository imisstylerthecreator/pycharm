from abc import abstractmethod
class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def __str__(self):
        return self.name


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


class Song:
    def __init__(self, title, duration, album):
        self.title = title
        self.duration = duration
        self.album = album

    def get_details(self):
        return f"{self.title} - {self.album.artist.name} [{self.duration} mins] from {self.album}"
    @abstractmethod
    def __str__(self):
        return self.title


class Playlist(Song):
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"{song.title} is added to playlist '{self.name}'")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song.title} is removed from playlist '{self.name}'")
        else:
            print(f"{song.title} not found in playlist '{self.name}'")

    def show_playlist(self):
        print(f"- {self.name}")
        for song in self.songs:
            print(f" - {song.get_details()}")

    def __str__(self):
        return self.name


class Subscription:
    def __init__(self, plan_name, price, benefits, can_skip_ads=None,can_skip_songs=None):
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


class User:
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
                return

        new_user = cls(username, password, subscription)
        print(f"User {username} signed in with subscription: {subscription.plan_name}.")
        return new_user

    def create_playlist(self, name):
        new_playlist = Playlist(name)
        self.playlists.append(new_playlist)
        print(f"Playlist '{name}' created for user '{self.username}'")
        return new_playlist

    def show_playlists(self):
        print(f"User '{self.username}' Playlists:")
        for playlist in self.playlists:
            playlist.show_playlist()

    def play_song(self, song):
        if self.subscription.can_skip_ads:
            print(f"{song.title} is playing without ads...")
        else:
            print(f"{song.title} is currently playing")


def main_menu():
    while True:
        print("1/ sign in")
        print("2/ log in")
        print("3/ exit")
        choice = input("choose: ")

        if choice == "1":
            username = input("enter username: ")
            password = input("enter password: ")
            plan = input("choose subscription (free/premium): ")

            if plan == "free":
                subscription = FreeSubscription()
            elif plan == "premium":
                subscription = PremiumSubscription()
            else:
                print("error")
                continue

            User.signin(username, password, subscription)

        elif choice == "2":
            username = input("enter username: ")
            password = input("enter password: ")
            user = User.login(username, password)

            if user:
                user_menu(user)

        elif choice == "3":
            print("logged out")
            break

def user_menu(user):
    while True:
        print("1/ create playlist")
        print("2/ show playlists")
        print("3/ add song to playlist")
        print("4/ play song")
        print("5/ subscription status")
        print("6/ logout")
        choice = input("choose: ")

        if choice == "1":
            playlist_name = input("enter playlist name: ")
            user.create_playlist(playlist_name)

        elif choice == "2":
            user.show_playlists()

        elif choice == "3":
            playlist_name = input("enter the playlist name: ")
            song_title = input("enter the song title: ")
            duration = input("enter the duration name: ")

            selected_playlist = None
            for playlist in user.playlists:
                if playlist.name == playlist_name:
                    selected_playlist = playlist
                    break

            if selected_playlist:
                new_song = Song(song_title, duration, None)
                selected_playlist.add_song(new_song)
                print(f"'{song_title}' has been added")
            else:
                print(f"playlist not found")

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
                print(f"Subscription Plan: {user.subscription.plan_name}")

        elif choice == "6":
            print("Logged out.")
            break

        else:
            print("Invalid choice!")


main_menu()
'''User.register(Subscription)
print(issubclass(Subscription, User))
tryout = Subscription('free')
print(isinstance(tryout, User))'''
'''playlist1 = Playlist('eve')
print(Playlist.__str__(playlist1))'''
