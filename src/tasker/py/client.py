from httpx import Client


class TaskerPyClient(Client):
    def __init__(
            self,
            address = "localhost",
            port = 9170,
        ):

        super().__init__(
            base_url=f"http://{address}:{port}",
            timeout=30,
        )
