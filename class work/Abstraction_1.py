from abc import ABC , abstractmethod

class Upload(ABC):
    @abstractmethod
    def compress(self):
        pass

class Image(Upload):
    def compress(self):
        print("Image is compressed to 2MB")

class Reel(Upload):
    def compress(self):
        print("Reel is compressed to 3MB")

r = Reel()
i = Image()
r.compress()
i.compress()

