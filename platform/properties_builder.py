from platform.detection.platform_detection import PlatformDetection
from platform.generic.generic_properties import GenericProperties
from platform.interfaces.properties_interface import PropertiesInterface
from platform.linux.linux_properties import LinuxProperties


class PropertiesBuilder(PlatformDetection):

    def __init__(self):
        super().__init__()

    def build(self) -> PropertiesInterface:
        if self.is_linux():
            return LinuxProperties()

        return GenericProperties()


