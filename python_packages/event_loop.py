import select

class EventLoop():
    def __init__(self):
        self.readers = []
    def add_reader(self, reader):
        self.readers.append(reader)
    def run_forever(self):
        while True:
            readers, _, _ = select.select(self.readers, [], [])

            for reader in readers:
                reader.on_read()
