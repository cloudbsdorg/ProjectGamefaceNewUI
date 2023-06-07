from gameface.interfaces.state.state import StatefulApplication


class ApplicationState(StatefulApplication):

    def __init__(self) -> None:
        super().__init__()

    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ApplicationState, cls).__new__(cls)
        return cls.instance

