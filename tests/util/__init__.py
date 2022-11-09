from shared import Document


class MyDocument(Document):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__read_done = False
        self.__write_done = False

    @property
    def read_done(self):
        return self.__read_done

    @property
    def write_done(self):
        return self.__write_done

    def _read(self):
        super()._read()
        self.__read_done = True

    def _write(self, data):
        super()._write(data)
        self.__write_done = True
