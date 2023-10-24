from pydantic import BaseModel

from datetime import datetime

# Get the current date and time
now = datetime.now()


"""
{'pk': 1903424587,
 'username': 'example',
 'full_name': 'Example Example',
 'is_private': False,
 'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/123884060_803537687159702_2508263208740189974_n.jpg?...', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', ...'),
 'is_verified': False,
 'media_count': 102,
 'follower_count': 576,
 'following_count': 538,
 'biography': 'Engineer: Python, JavaScript, Erlang',
 'external_url': HttpUrl('https://example.org/', scheme='https', host='example.org', tld='com', host_type='domain', path='/'),
 'is_business': False}
"""


class User(BaseModel):
    username: str
    full_name: str
    is_private: bool
    is_verified: bool
    media_count: int
    follower_count: int
    is_business: bool
    biography: str
    interests: list[str]
    timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")  # Date time formatting


class Users(BaseModel):
    user_list: list[User]
