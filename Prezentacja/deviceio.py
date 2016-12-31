import os
class IODevice:
    def __init__(self, path_to_device):
        self.path_to_device = path_to_device
        self.file_descriptor = os.open(path_to_device, os.O_RDWR | O_NOCITY)

    def write(self, command):
        os.write(self.file_descriptor, command)

    def read(self, length=4000):
        return os.read(self.file_descriptor, length)

    def close(self):
        os.close(self.file_descriptor)

device = IODevice("/dev/usbtmc0")
device.write("*IDN?")
print(device.read())

