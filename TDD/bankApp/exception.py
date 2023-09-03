class PinError(Exception):
    def __init__(self, message: object) -> None:
        super().__init__(message)


class EntryError(Exception):
    def  __init__(self, message: object) -> None:
        super().__init__(message)

class AmountLessThanZero(Exception):

    def   __init__(self, message: object) -> None:
        super().__init__(message)


class AmountIsGreaterThanBalance(Exception):
    def __init__(self, message: object) -> None:
        super().__init__(message)

