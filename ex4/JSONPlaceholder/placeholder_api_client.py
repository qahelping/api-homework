import requests


class PlaceholderApiClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/"
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}

    def get_posts(self):
        response = self.session.get(url=f"{self.base_url}posts")
        return response

    def get_post_comments(self, post_id):
        response = self.session.get(url=f"{self.base_url}posts/{post_id}/comments")
        return response

    def get_albums(self):
        response = self.session.get(url=f"{self.base_url}albums")
        return response

    def get_album(self, album_id):
        url = f"{self.base_url}albums/{album_id}"
        response = self.session.get(url=url)
        return response

    def get_photos(self):
        response = self.session.get(url=f"{self.base_url}photos")
        return response

    def get_photo(self, photo_id):
        response = self.session.get(url=f"{self.base_url}photos/{photo_id}")
        return response

    def get_users(self):
        response = self.session.get(url=f"{self.base_url}users")
        return response

    def get_todos(self, user_id=0):
        url = f"{self.base_url}todos"
        if user_id:
            self.session.params = {"userId": user_id}
        response = self.session.get(url=url)
        return response


