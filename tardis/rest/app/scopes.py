from enum import Enum

# All available OAuth2 scopes


class Resources(str, Enum):
    get = "resources:get"
    put = "resources:put"


class User(str, Enum):
    get = "user:get"
    put = "user:put"  # usused
