import UI
import function


def start():
    while True:
        button = UI.menu()
        if button == 1:
            function.loading()
        elif button == 2:
            function.add()
        elif button == 3:
            function.delete()
        elif button == 4:
            function.export()
        elif button == 5:
            print('Выход')
            break
        else:
            print('Повторите ввод')
