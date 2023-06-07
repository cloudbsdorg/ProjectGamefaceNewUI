from gameface.interfaces.state.state import StatefulApplication
from gameface.interfaces.ui.customwindowinterface import CustomWindowInterface


class GameFaceFace(CustomWindowInterface):
    def __init__(self) -> None:
        super().__init__()
        self.title("Project GameFACE XX.XX.XX")
        self.geometry(f"{1100}x{580}")
