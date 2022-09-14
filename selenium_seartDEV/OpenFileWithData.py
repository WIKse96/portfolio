import json


class OpenFileWithData:
    def __init__(self, filePath):
        self.filePath = filePath
        self.data = None

    def open(self):
        with open(self.filePath, 'r') as fileWithLogin:
            self.data = fileWithLogin.read()
            return json.loads(self.data)



