import requests


class Page:
    def __init__(self, page_id, page_token=None, user_token=None):
        if page_token is None and user_token is None:
            raise Exception("'page_token' or 'user_token' must set")
        self.page_token = page_token
        self.page_id = page_id
        self.user_token = user_token
        if page_token is None:
            self.page_token = self.get_page_token(page_id)
            print(f"Get page token ok. Page token is: {self.page_token}")

    def get_page_token(self, page_id):
        end_point = f"https://graph.facebook.com/{page_id}"
        params = {
            'fields': 'access_token',
            'access_token': self.user_token
        }
        response = requests.get(end_point, params=params)
        if response.status_code != 200:
            raise Exception(
                f'Cannot get page token from page {page_id}, status code: {response.status_code}, message: {response.json()}')
        response = response.json()
        data = response.get("access_token")
        return data

    def get_comments(self, post_id):
        host = "https://graph.facebook.com"
        end_point = f"{host}/{post_id}/comments"

        params = {
            "access_token": self.page_token,
            "limit": 2000
        }
        response = requests.get(end_point, params=params)
        try:
            if response.status_code != 200:
                raise Exception(
                    f'Cannot get comment from post {post_id}, status code: {response.status_code}, message: {response.json()}')
            response = response.json()
            data = response.get("data")
            return data
        except Exception as e:
            print(f"Error when get comment from {post_id}, {e}")
            return []

    # def get_replies(self, comment_id):
    #     host = "https://graph.facebook.com"
    #     end_point = f"{host}/{comment_id}/comments"
    #     params = {
    #         "access_token": self.page_token,
    #         "limit": 2000
    #     }
    #     response = requests.get(end_point, params=params)
    #     if response.status_code != 200:
    #         raise Exception(
    #             f'Cannot get comment from post {comment_id}, status code: {response.status_code}, message: {response.json()}')
    #     response = response.json()
    #     data = response.get("data")
    #     return data

    def get_comment_with_replies(self, post_id):
        comments = self.get_comments(post_id)
        all_comments = comments.copy()
        for comment in comments:
            comment_id = comment.get('id')
            if comment_id is not None:
                sub_comments = self.get_comment_with_replies(comment_id)
                if len(sub_comments) > 0:
                    all_comments += sub_comments
        return all_comments

    def send_message_to_user(self, user_id, message):
        end_point = 'https://graph.facebook.com/me/messages'
        params = {
            "access_token": self.page_token
        }
        headers = {"Content-Type": "application/json"}
        try:
            body = {
                "messaging_type": "<MESSAGING_TYPE>",
                "recipient": {
                    "id": str(user_id)
                },
                "message": {
                    "text": message
                }
            }
            return True
        except Exception as e:
            print(f"Cannot send message to {user_id}, {e}")
            return False
