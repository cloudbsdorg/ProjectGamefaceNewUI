from enum import Enum


class State(Enum):
    READY = 0
    ERROR = 1
    STARTED = 2
    NOT_STARTED = 3
    INITIALIZED = 4
    INITIALIZATION_FAILURE = 5

    def __init__(self) -> None:
        super().__init__()

    def __init__(self, ex) -> None:
        super().__init__()

class StatefulApplication:

    def __init__(self) -> None:
        super().__init__()
        self.application_states: dict[str, State] = {}

    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(StatefulApplication, cls).__new__(cls)
        return cls.instance

    def set_state(self, name: str, state: State):
        self.application_states[name] = state
