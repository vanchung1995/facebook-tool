import requests
class Page:
    def __init__(self, page_token):
        self.page_token = page_token

    def send_message_to_user(self, user_id, message):
        end_point = 'https://graph.facebook.com/me/messages'
        params = {
            "access_token": self.page_token
        }
        try:
            headers = {""}
            return True
        except Exception as e:
            print(f"Cannot send message to {user_id}, {e}")
            return False
