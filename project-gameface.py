from gameface.gamefaceface import GameFaceFace
from gameface.state.application_state import ApplicationState


class Main:

    def __init__(self) -> None:
        super().__init__()
        self.state = ApplicationState()

    def start(self):
        app = GameFaceFace()
        app.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main = Main()
    main.start()
