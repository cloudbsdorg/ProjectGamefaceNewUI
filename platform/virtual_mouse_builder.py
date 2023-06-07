import sys

from platform.detection.platform_detection import PlatformDetection
from platform.interfaces import mouse_interface
if sys.platform != "win32":
    from platform.generic.generic_virtual_mouse import GenericVirtualMouse
if sys.platform == "win32":
    from platform.windows.windows_virtual_mouse import WindowsVirtualMouse


class VirtualMouseBuilder(PlatformDetection):

    def __init__(self):
        super().__init__()

    def build(self) -> mouse_interface:
        if self.is_windows():
            return WindowsVirtualMouse()
        else:
            return GenericVirtualMouse()


