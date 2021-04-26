import requests
class PostComment:
    def __init__(self, user_access_token):
        self.user_access_token = user_access_token

    def get_page_token(self, page_id):
        end_point = f"https://graph.facebook.com/{page_id}"
        params = {
            'fields': 'access_token',
            'access_token': self.user_access_token
        }
        response = requests.get(end_point, params=params)
        if response.status_code != 200:
            raise Exception(f'Cannot get page token from page {page_id}, status code: {response.status_code}, message: {response.json()}')
        response = response.json()
        data = response.get("access_token")
        return data

    def get_comments(self, post_id):
        host = "https://graph.facebook.com"
        end_point = f"{host}/{post_id}/comments"
        params = {
            "access_token": self.user_access_token,
            "limit":2000
        }
        response = requests.get(end_point, params=params)
        if response.status_code != 200:
            raise Exception(f'Cannot get comment from post {post_id}, status code: {response.status_code}, message: {response.json()}')
        response = response.json()
        data = response.get("data")
        return data

    def get_comment_with_replies(self, comment_id):
        host = "https://graph.facebook.com"
        end_point = ""
