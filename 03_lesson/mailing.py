from address import Address


class Mailing:

    def __init__(self, to_address: Address, from_address: Address,
                 cost: float, track: str):
        self.to_address: Address = to_address
        self.from_address: Address = from_address
        self.cost: float = cost
        self.track: str = track
