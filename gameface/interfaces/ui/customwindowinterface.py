import customtkinter

from platform.detection.platform_detection import PlatformDetection


class CustomWindowInterface(customtkinter.CTk, PlatformDetection):

    def __init__(self) -> None:
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        super().__init__()