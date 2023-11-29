import LocalPokedex.Controller.MainController as Mc
import LocalPokedex.Controller.ShowPkmController as Sp
import LocalPokedex.Controller.ComparatorController as Sc

if __name__ == "__main__":
    import sys
    app = Mc.QtWidgets.QApplication([])
    stack = Mc.QtWidgets.QStackedWidget()

    showMain = Mc.ShowMain()
    showPkm = Sp.ShowPkm()
    showComparator = Sc.ShowComparator()

    showMain.stack.setFixedWidth(800)
    showMain.stack.setFixedHeight(600)

    showMain.stack.addWidget(showMain)
    showMain.stack.addWidget(showPkm)
    showMain.stack.addWidget(showComparator)

    showMain.stack.show()
    sys.exit(app.exec())

