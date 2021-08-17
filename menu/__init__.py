from figures import FigureTypes
from figures.figures import create_Figure

from manager import manager
from file.file import create_Operation
from file.constants import OperationTypes
from view import g_view


#figures
def showFigures():
    figures = manager.getFigures()
    if any(figures) == True:
        for key, figure in manager.getFigures().items():
            data = figure.getDescription()
            g_view.showMessage(f'ID: {key}, {data}')
    else:
        g_view.showMessage('Нет фигур')

def createRect(wigth, lenght):
    manager.addFigure(create_Figure(FigureTypes.RECT, wigth, lenght))

def createTrian(side1, side2, side3):
    manager.addFigure(create_Figure(FigureTypes.TRIAN, side1, side2, side3))

def createSqu(side):
    manager.addFigure(create_Figure(FigureTypes.SQU, side))

def createCirc(diameter):
    manager.addFigure(create_Figure(FigureTypes.CIRC, diameter))

Type_operations = {
    'save': OperationTypes.Save,
    'create': OperationTypes.Create,
    'del': OperationTypes.Delete
}

#Project
def saveProj(filename):
    create_Operation(OperationTypes.Save, filename)

def createProj(filename):
    create_Operation(OperationTypes.Create, filename)

def deleteProj(filename):
    create_Operation(OperationTypes.Delete, filename)

def loadProj(filename):
    create_Operation(OperationTypes.Load, filename)

#calculate func
def S(ID):
    if ID in manager.getFigures():
        figure = manager.getFigure(ID)
        g_view.showMessage(figure.square())
    else:
        g_view.showMessage('No figure with this ID')


def P(ID):
    if ID in manager.getFigures():
        figure = manager.getFigure(ID)
        g_view.showMessage(figure.perimeter())
    else:
        g_view.showMessage('No figure with this ID')


