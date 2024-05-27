from typing import Any
from blog.data import posts


def test_return_all_content():# request: HttpRequest, post_id: int

    # print('posts', posts)
    assert len(posts) == 100

def test_return_post():# request: HttpRequest, post_id: int
    found_post: dict[str, Any] | None = None

    post_id = 1

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    # print('found_post.title', found_post["title"])
    assert found_post["title"] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
