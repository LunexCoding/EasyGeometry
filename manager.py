from IDGenerator import getID
from figures.figures import BaseFigure
from excections import majorException


CURRENT_VERSION = 1.0


class FigureManager:

    def __init__(self):
        self.__figures = {}

    def addFigure(self, figure):
        figId = getID()
        self.__figures[figId] = figure
        return figId

    def getFigures(self):
        return self.__figures

    def getFigure(self, figureId):
        return self.__figures.get(figureId)

    def getDataForSerialization(self):
        data = []
        for figure in self.__figures.values():
            data.append(figure.getDataForSerialization())
        return data

    def restoreFiguresFromSerializedData(self, data):
        try:
            for line in data:
                figure = BaseFigure.createFigureFromSerializationData(str(line).replace('\n', ''))
                if figure is not None:
                    manager.addFigure(figure)
        except majorException as e:
            print(e)
            self.clear()
            return False
        return True

    def clear(self):
        self.__figures.clear()


manager = FigureManager()
