from view import g_view
from excections import majorException

class MenuElement:
    def __init__(self, command, description, callback, arguments=[]):
        self._command = command
        self._description = description
        self._callback = callback
        self._arguments = arguments
        self._parrent = None

    def getCommand(self):
        return self._command

    def setParrent(self, parrent):
        self._parrent = parrent

    def __repr__(self):
        return '{}: {}'.format(self._command, self._description)

    def __call__(self, *args):
        try:
            if self._callback is not None:
                if len(args) == len(self._arguments):
                    self._callback(*self.__convertArguments(*args))
                else:
                    g_view.showMessage("wrong arguments: " + 'number ' * len(self._arguments))
            return self._parrent
        except majorException as e:
            g_view(e)
            return self._parrent

    def __convertArguments(self, *args):
        try:
            return [self._arguments[index](arg) for index, arg in enumerate(args)]
        except:
            raise majorException("wrong arguments: " + 'number ' * len(self._arguments))


class Menu(MenuElement):
    def __init__(self, command='', description='', elements=[]):
        super(Menu, self).__init__(command, description, self)
        self._elements = {element.getCommand(): element for element in elements}

    def addElement(self, element):
        element.setParrent(self)
        self._elements[element.getCommand()] = element

    def execute(self, input):
        args = input.split(' ')
        command = args[0]
        del args[0]

        if command in self._elements:
            return self._elements[command](*args)
        else:
            g_view.showMessage('wrong command: {}'.format(command))
        return self

    def show(self):
        for element in self._elements.values():
            print(str(element))

    def __call__(self, *args):
        return self
