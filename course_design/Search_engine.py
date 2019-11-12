import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from Ui_mainWindow import *
from spider import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.sp = Spider()
        url = "https://news.sina.com.cn/"
        self.sp.get_sites(url, 3)
        self.sp.page_rank(0.5)
        self.se = SearchEngine().from_spider(self.sp)
        self.print_list = []
        self.tbrList.setOpenExternalLinks(True)
        self.tbrList.setOpenLinks(True)
    def updateList(self):
        head = "<html><body>\n"
        tail = "</body></html>\n"
        self.tbrList.setHtml(head+"\n".join(self.print_list)+tail)
    def addItem(self, title, url):
        append = "<h1>"+title+"</h1>\n<a href="+'"'+url+'">'+url+"</a>"
        self.print_list.append(append)
        self.updateList()
    def not_found(self):
        self.print_list = "没有找到相关新闻！"
        QMessageBox.critical(self, "错误", "没有找到相关新闻！")
    def clear(self):
        self.print_list = []
        self.updateList()
    def search(self):
        txt = self.letKeyword.text()
        
        self.se.search(txt)
        tops = self.se.top(5)
        if(tops == None):
            self.not_found()
            return
        self.clear()
        for i in tops:
            art = self.sp.webs.article[i[0]]
            self.addItem(art.title, i[0])
            # self.addItem(self.sp.webs.article[i[0]].title)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.btnSearch.clicked.connect(myWin.search)
    myWin.show()
    sys.exit(app.exec_())


"""
TODO
    - [functional]input needs to be parsed before matched
    - [new feature]add some imformation when it is collecting the data
    - [fix] if the input is not matched, runtime error occurs
    - [new feature] try to draw a more nice interface, and support hypertext
"""