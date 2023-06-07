import sys

from platform.detection.platform_detection import PlatformDetection
from platform.interfaces.display_interface import DisplayInterface
from platform.generic.generic_display import GenericDisplay

if sys.platform == 'darwin':
    from platform.darwin.darwin_display import DarwinDisplay
if sys.platform == 'win32':
    from platform.windows.windows_display import WindowsDisplay


class DisplayBuilder(PlatformDetection):

    def __init__(self):
        super().__init__()

    def build(self) -> DisplayInterface:
        if self.is_windows():
            return WindowsDisplay()
        elif self.is_darwin():
            return DarwinDisplay()
        else:
            return GenericDisplay()
