from platform.detection.platform_detection import PlatformDetection
from platform.generic.generic_camera import GenericCamera
from platform.interfaces.camera_interface import CameraInterface
from platform.windows.windows_camera import WindowsCamera


class CameraBuilder(PlatformDetection):

    def __init__(self):
        super().__init__()

    def build(self) -> CameraInterface:
        if self.is_windows():
            return WindowsCamera()

        return GenericCamera()


