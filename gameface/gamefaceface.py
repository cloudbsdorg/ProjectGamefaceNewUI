from gameface.interfaces.customwindowinterface import CustomWindowInterface
import tkinter
import tkinter.messagebox
import customtkinter


class GameFaceFace(CustomWindowInterface):
    def __init__(self) -> None:
        super().__init__()
        self.title("Project GameFACE XX.XX.XX")
        self.geometry(f"{1100}x{580}")
