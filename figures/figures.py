from figures import FigureTypes
from math import sqrt
from excections import majorException
from view import g_view


class BaseFigure(object):

    def getMessage(self):
        raise NotImplementedError()

    def perimeter(self):
        return self._perimeter()

    def square(self):
        return self._square()

    @staticmethod
    def createFigureFromSerializationData(data):
        figureType = BaseFigure.unpackFigureType(data[0])
        if figureType not in figureByType:
            print('wrong figure type: {}'.format(figureType))
            return None
        return figureByType[figureType](serializationData=data)

    def getDataForSerialization(self):
        raise NotImplementedError()

    def restoreFigureFromSerializationData(self):
        raise NotImplementedError()

    def getDescription(self):
        pass

    def _perimeter(self):
        raise NotImplementedError()

    def _square(self):
        raise NotImplementedError()

    @staticmethod
    def packFigureType(figureType):
        return chr(figureType)

    @staticmethod
    def unpackFigureType(char):
        return ord(char)


class Rectangle(BaseFigure):

    def __init__(self, width=0, lenght=0, serializationData=None):
        self.init(width, lenght, serializationData)

    def init(self, width=0, lenght=0, serializationData=None):
        if serializationData is not None:
            self.restoreFigureFromSerializationData(serializationData)
        else:
            self._width = int(width)
            self._length = int(lenght)
            g_view.showMessage(self.getMessage())

    def getMessage(self):
        return 'Rectangle created.'

    def _perimeter(self):
        return f'P = {(self._width + self._length) * 2}'

    def _square(self):
        return f'S = {self._width * self._length}'

    def getDataForSerialization(self):
        data = '{} {} {}'.format(BaseFigure.packFigureType(FigureTypes.RECT), self._width, self._length)
        return data

    def restoreFigureFromSerializationData(self, data):
        assert BaseFigure.unpackFigureType(data[0]) == FigureTypes.RECT
        try:
            _, self._width, self._length = data.split(' ')
        except:
            raise majorException('Loading is not possible. Damaged file')

    def getDescription(self):
        data = 'Прямоуольник, стороны: {}, {}'.format(self._width, self._length)
        return data


class Triangle(BaseFigure):

    def __init__(self, side1=0, side2=0, side3=0, serializationData=None):
        self.init(side1, side2, side3, serializationData)

    def init(self, side1=0, side2=0, side3=0, serializationData=None):
        if serializationData is not None:
            self.restoreFigureFromSerializationData(serializationData)
        else:
            self._side1 = int(side1)
            self._side2 = int(side2)
            self._side3 = int(side3)
            g_view.showMessage(self.getMessage())

    def getMessage(self):
        return 'Triangle created.'

    def perimeter(self):
        return f'P = {self._side1 + self._side2 + self._side3}'

    def square(self):
        halfP = (self._side1 + self._side2 + self._side3) / 2
        Square_area = (halfP * (halfP - self._side1) * (halfP - self._side2) * (halfP - self._side3))
        if Square_area <= 0:
            return 'Такого треугольника не существует!'
        S = round(sqrt(Square_area), 2)
        return f'S = {S}'

    def getDataForSerialization(self):
        data = '{} {} {} {}'.format(BaseFigure.packFigureType(FigureTypes.TRIAN), self._side1, self._side2, self._side3)
        return data

    def restoreFigureFromSerializationData(self, data):
        assert BaseFigure.unpackFigureType(data[0]) == FigureTypes.TRIAN
        try:
            _, self._side1, self._side2, self._side3 = data.split(' ')
        except:
            raise majorException('Loading is not possible. Damaged file')

    def getDescription(self):
        data = 'Треугольник, стороны: {}, {}, {}'.format(self._side1, self._side2, self._side3)
        return data


class Circle(BaseFigure):

    def __init__(self, diameter=0, serializationData=None):
        self.init(diameter, serializationData)

    def init(self, diameter=0, serializationData=None):
        if serializationData is not None:
            self.restoreFigureFromSerializationData(serializationData)
        else:
            self._diameter = int(diameter)
            g_view.showMessage(self.getMessage())

    def getMessage(self):
        return 'Circle created.'

    def perimeter(self):
        return f'P = {round(self._diameter * 3.14, 2)}'

    def square(self):
        return f'S = {round((0.25 * 3.14) * (self._diameter ** 2), 2)}'

    def getDataForSerialization(self):
        data = '{} {}'.format(BaseFigure.packFigureType(FigureTypes.CIRC), self._diameter)
        return data

    def restoreFigureFromSerializationData(self, data):
        assert BaseFigure.unpackFigureType(data[0]) == FigureTypes.CIRC
        try:
            _, self._diameter = data.split(' ')
        except:
            raise majorException('Loading is not possible. Damaged file')

    def getDescription(self):
        data = 'Круг, диаметр: {}'.format(self._diameter)
        return data


class Square(BaseFigure):

    def __init__(self, side=0, serializationData=None):
        self.init(side, serializationData)

    def init(self, side=0, serializationData=None):
        if serializationData is not None:
            self.restoreFigureFromSerializationData(serializationData)
        else:
            self._side = int(side)
            g_view.showMessage(self.getMessage())

    def getMessage(self):
        return "Square created."

    def perimeter(self):
        return f'P = {self._side * 4}'

    def square(self):
        return f'S = {self._side ** 2}'

    def getDataForSerialization(self):
        data = '{} {}'.format(BaseFigure.packFigureType(FigureTypes.SQU), self._side)
        return data

    def restoreFigureFromSerializationData(self, data):
        assert BaseFigure.unpackFigureType(data[0]) == FigureTypes.SQU
        try:
            _, self._side = data.split(' ')
        except:
            raise majorException('Loading is not possible. Damaged file')

    def getDescription(self):
        data = 'Квадрат, сторона: {}'.format(self._side)
        return data


class NoneFigure(BaseFigure):

    def __init__(self):
        self.get_message()

    def get_message(self):
        return "We cannot create such a figure."


figureByType = {
    FigureTypes.RECT: Rectangle,
    FigureTypes.CIRC: Circle,
    FigureTypes.TRIAN: Triangle,
    FigureTypes.SQU: Square,
    FigureTypes.DEF: NoneFigure
}



def create_Figure(*data):
    getData = list(data)
    typeFigure = getData.pop(0)
    sides = getData
    return figureByType[typeFigure](*sides)
