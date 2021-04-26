import requests
class PostComment:
    def __init__(self, user_access_token):
        self.access_token = user_access_token

    def get_comments(self, post_id):
        host = "https://graph.facebook.com"
        end_point = f"{host}/{post_id}/comments"
        params = {
            "access_token": self.access_token,
            "limit":2000
        }
        response = requests.get(end_point, params=params)
        print(response.url)
        if response.status_code != 200:
            raise Exception(f'Cannot get comment from post {post_id}, status code: {response.status_code}, message: {response.json()}')
        response = response.json()
        data = response.get("data")
        return data

    def get_comment_with_replies(self, comment_id):
        host = "https://graph.facebook.com"
        end_point = ""
