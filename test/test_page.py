from core.page import Page
import os
import json

if __name__ == '__main__':
    page_id = 913770675483798
    user_token = os.environ.get('FB_TOKEN')
    page_token = os.environ.get('PAGE_TOKEN')
    if user_token is None and page_token is None:
        print("set FB_TOKEN, PAGE_TOKEN environment to your access token fb")
        exit(0)
    page_inst = Page(page_id=page_id, user_token=user_token, page_token=page_token)
    post_id = 941483042712561
    # post_id = '941483042712561_941736682687197'

    comments = page_inst.get_comments(post_id)
    # print(json.dumps(comments, indent=4, ensure_ascii=False))

    comment_id = '941483042712561_941736682687197'
    replies = page_inst.get_comments(comment_id)
    # print(json.dumps(replies, indent=4, ensure_ascii=False))

    all_comments_with_replies = page_inst.get_comment_with_replies(post_id)
    print(json.dumps(all_comments_with_replies, indent=4, ensure_ascii=False))

    for cmt in all_comments_with_replies:
        print(cmt.get("message"))

    user_id = 100005103257451 # truonghang
    message = "Hello Hang Ham"

