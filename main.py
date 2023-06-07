from gameface.gamefaceface import GameFaceFace


class Main:

    def __init__(self) -> None:
        super().__init__()

    def start(self):
        app = GameFaceFace()
        app.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main = Main()
    main.start()
