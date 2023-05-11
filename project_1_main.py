from project_1 import *

def main():
    app = QApplication([])
    window = Controller()
    window.setGeometry(200, 200, 900, 500)
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()



