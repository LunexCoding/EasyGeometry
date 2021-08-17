from menu.menu import Menu, MenuElement
from menu import *
from downloader import showMsg


mainMenu = Menu('main', 'main menu')


figuresMenu = Menu('fig', 'figures operations')
mainMenu.addElement(figuresMenu)
figuresMenu.addElement(MenuElement('show', 'show figures', showFigures))
figuresMenu.addElement(MenuElement('rect', 'creates rectangle', createRect, [int, int]))
figuresMenu.addElement(MenuElement('trian', 'creates triangle', createTrian, [int, int, int]))
figuresMenu.addElement(MenuElement('squ', 'creates square', createSqu, [int]))
figuresMenu.addElement(MenuElement('circ', 'creates circle', createCirc, [int]))


calculateFunctionMenu = Menu('calc', 'function calculation')
calculateFunctionMenu.addElement(MenuElement('s', 'calculate area', S, [int]))
calculateFunctionMenu.addElement(MenuElement('p', 'calculate perimeter', P, [int]))


projectOperations = Menu('pr', 'project operations')
mainMenu.addElement(projectOperations)
projectOperations.addElement(MenuElement('save', 'save project', saveProj, [str]))
projectOperations.addElement(MenuElement('create', 'create project', createProj, [str]))
projectOperations.addElement(MenuElement('delete', 'delete project', deleteProj, [str]))
projectOperations.addElement(MenuElement('load', 'load project', loadProj, [str]))


figuresMenu.addElement(projectOperations) # добавили подменю проекта в меню с фигурами
figuresMenu.addElement(calculateFunctionMenu) # добавили подменю функции расчета в меню с фигурами
calculateFunctionMenu.addElement(mainMenu)
figuresMenu.addElement(mainMenu)
projectOperations.addElement(figuresMenu) # добавили подменю фигур в меню с проектом
projectOperations.addElement(mainMenu)


currentMenu = mainMenu
prevMenu = None


if __name__ == "__main__":
    g_view.showMessage(showMsg)
    while True:
        if currentMenu != prevMenu: # чтобы отображалось меню, только если мы перешли в саб меню. А то сильно много спама
            currentMenu.show()
        prevMenu = currentMenu
        currentMenu = currentMenu.execute(input(': '))
