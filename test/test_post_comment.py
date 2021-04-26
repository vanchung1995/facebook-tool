from core.comment_post import PostComment
import os
import json
if __name__ == '__main__':
    user_token = os.environ.get('FB_TOKEN')
    page_token = os.environ.get('PAGE_TOKEN')
    if user_token is None and page_token is None:
        print("set FB_TOKEN, PAGE_TOKEN environment to your access token fb")
        exit(0)
    page_id = 913770675483798
    post_comment_inst = PostComment(user_access_token=user_token, page_token=page_token)
    post_id = 941483042712561
    # post_id = '941483042712561_941736682687197'

    comments = post_comment_inst.get_comments(post_id)
    print(json.dumps(comments, indent=4,ensure_ascii=False))
    # print(post_comment_inst.get_page_token(page_id))
