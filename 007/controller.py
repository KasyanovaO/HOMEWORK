import UI
import function


def start():
    button = UI.menu()
    if button == 1:
        function.viewing()
    elif button == 2:
        function.search()
    elif button == 3:
        function.export()
    elif button == 4:
        print('Выход')
    else:
        print('Повторите ввод')
        start()
