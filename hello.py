Jannat Ibrahim, [11/20/2024 7:16 PM]
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

    def __str__(self):
        return self.title


class Playlist:
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
    def __init__(self, plan_name, price, benefits, can_skip_ads=False, can_skip_songs=False):
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
        self._password = password  # Sensitive data
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
            print(f"{song.

Jannat Ibrahim, [11/20/2024 7:16 PM]
title} is currently playing")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Sign In")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            plan = input("Choose subscription (free/premium): ").lower()

            if plan == "free":
                subscription = FreeSubscription()
            elif plan == "premium":
                subscription = PremiumSubscription()
            else:
                print("Invalid subscription type!")
                continue

            User.signin(username, password, subscription)

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
            print("Invalid choice!")


def user_menu(user):
    while True:
        print(f"\n--- User Menu ({user.username}) ---")
        print("1. Create Playlist")
        print("2. Show Playlists")
        print("3. Play Song")
        print("4. Log Out")
        choice = input("Choose an option: ")

        if choice == "1":
            playlist_name = input("Enter playlist name: ")
            user.create_playlist(playlist_name)

        elif choice == "2":
            user.show_playlists()

        elif choice == "3":
            song_title = input("Enter song title to play: ")
            for playlist in user.playlists:
                for song in playlist.songs:
                    if song.title == song_title:
                        user.play_song(song)
                        break

        elif choice == "4":
            print("Logged out.")
            break

        else:
            print("Invalid choice!")


# Start the application
main_menu()