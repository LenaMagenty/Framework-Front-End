class UrlHelper:
    @staticmethod
    def with_basic_auth(url: str, username: str, password: str) -> str:
        return url.replace('://', f'://{username}:{password}@', 1)
