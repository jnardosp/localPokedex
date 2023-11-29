import Controller.MainController as Mc
import Controller.ShowPkmController as Sp
import Controller.ComparatorController as Sc
import Controller.HeapController as Hc

if __name__ == "__main__":
    import sys
    app = Mc.QtWidgets.QApplication([])
    stack = Mc.QtWidgets.QStackedWidget()

    showMain = Mc.ShowMain()
    showPkm = Sp.ShowPkm(showMain)
    showHeap = Hc.ShowHeap(showMain)
    showComparator = Sc.ShowComparator(showMain)

    showMain.stack.setFixedWidth(800)
    showMain.stack.setFixedHeight(600)

    showMain.stack.addWidget(showMain)
    showMain.stack.addWidget(showPkm)
    showMain.stack.addWidget(showHeap)
    showMain.stack.addWidget(showComparator)

    showMain.stack.show()
    sys.exit(app.exec())

