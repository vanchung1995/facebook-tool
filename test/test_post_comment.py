from core.comment_post import PostComment
import os
import json
if __name__ == '__main__':
    fb_token = os.environ.get('FB_TOKEN')
    if fb_token is None:
        print("set FB_TOKEN environment to your access token fb")
        exit(0)
    post_comment_inst = PostComment(fb_token)
    post_id = 945423958985136
    post_id = '945423958985136_945424528985079'
    post_id = '945423958985136_968760849984780'
    comments = post_comment_inst.get_comments(post_id)
    print(json.dumps(comments, indent=4,ensure_ascii=False))