from manager import manager, CURRENT_VERSION
import os
from view import g_view
import os.path

from .constants import OperationTypes


try:
    os.mkdir('Projects')
    os.chdir('Projects')
except OSError:
    os.chdir('Projects')


class BaseFileOperation(object):

    def getMessage(self):
        raise NotImplementedError()


class Save(BaseFileOperation):

    def __init__(self, filename):
        self._filename = filename
        self.save()
        g_view.showMessage(self.getMessage())

    def getMessage(self):
      return f"File {self._filename} saved."

    def save(self):
        file_clear = open(self._filename, 'w').close()
        file = open(self._filename, 'a', encoding='UTF-8')
        file.write(str(CURRENT_VERSION) + '\n')
        data = manager.getDataForSerialization() 
        file.write('\n'.join(data))
        file.close()


class Delete(BaseFileOperation):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            self.delete()
            g_view.showMessage(self.get_message())
        else:
            g_view.showMessage('File not found.')

    def get_message(self):
        return f"File {self._filename} deleted."

    def delete(self):
        os.remove(self._filename)


class Create(BaseFileOperation):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            g_view.showMessage('The file has already been created.')
        else:
            self.create()
            g_view.showMessage(self.get_message())

    def get_message(self):
        return f"File {self._filename} created."

    def create(self):
        file = open(self._filename, 'w+', encoding='UTF-8')
        file.close()


class Load(BaseFileOperation):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            self.load()
            g_view.showMessage(self.get_message())
        else:
            g_view.showMessage('File not found.')

    def get_message(self):
        return f"File {self._filename} loaded."

    def load(self):
        file = open(self._filename, 'r', encoding='UTF-8')
        data = file.readlines()
        del data[0] # removes file version
        result = manager.restoreFiguresFromSerializedData(data)
        file.close()
        return result


operationByType = {
    OperationTypes.Save: Save,
    OperationTypes.Delete: Delete,
    OperationTypes.Create: Create,
    OperationTypes.Load: Load
}


def create_Operation(*OperationType):
    OperationType = list(OperationType)
    operation = OperationType[0]
    del OperationType[0]
    filename = ''.join(OperationType)
    return operationByType[operation](filename)