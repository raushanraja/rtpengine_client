import os
from dotenv import load_dotenv
load_dotenv()


class Env:

    def __init__(self) -> None:
        host = os.getenv('RTPENGINE_CLIENT_HOST')
        port = os.getenv('RTPENGINE_CLIENT_PORT')
        self.RTPENGINE_URL = f'{host}:{port}/ng'


env = Env()
