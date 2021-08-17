import requests, os
from manager import CURRENT_VERSION

class error(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __repr__(self):
        return self.__msg


class programVersion:


    version = CURRENT_VERSION


    def __init__(self, url):
        self._receivedVersion = None

        self._url = url
        if self.versionQuery() == True:
            self.getVersion()
            self.delete()

    def versionQuery(self):
        self._filename = self._url.split('/')[-1]
        self._r = requests.get(self._url)
        self._status = self._r.status_code
        if self._status == 404:
            return False
        elif self._status == 200:
            with open(self._filename, 'wb') as f:
                f.write(self._r.content)
            return True

    def getVersion(self):
        with open(self._filename, 'r') as f:
            self._receivedVersion = float(f.read())
            return self._receivedVersion

    def delete(self):
        os.remove(self._filename)

    def __repr__(self):
        if self._receivedVersion is not None:
            if self.version < self._receivedVersion:
                return f'You have an old version, to get access to new functions, update the program to the version {self._receivedVersion}.'
            else:
                return f'You have the optimal version {self.version} of the program.'
        else:
            return 'An error occurred while checking for updates.'


gitVersion = programVersion('https://raw.github.com/LunexCoding/EasyGeometry/main/version.txt')
showMsg = gitVersion