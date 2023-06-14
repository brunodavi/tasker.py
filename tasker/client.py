from httpx import Client


class TaskerClient(Client):
    def __init__(
            self,
            *,
            adderess = 'localhost',
            port = 9170,
        ):

        super().__init__(
            base_url=f'http://{adderess}:{port}',
            timeout=30,
        )

del Client
