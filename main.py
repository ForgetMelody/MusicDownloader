import time,sys,requests
#PyQt GUI

from PyQt5.QtWidgets import QApplication, QMainWindow
from Form import *
#获取ID的API
from GetID import *
#下载音乐的API
from Download import wangyiyun
class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
    #重写父类中的按钮点击事件
    def On_Download_Button_Clicked(self):
        _translate = QtCore.QCoreApplication.translate

        print("[Info]Download Button Clicked")
        SearchName = self.textEdit.toPlainText()
        print("[Info]Got text:{"+SearchName + "}")
        id, name =getSong(SearchName)
        #self.ID_Label.setText("ID:" + id)
        #self.Name_Label.setText("歌曲名:" + name)
        print("下载ID:",id,"\n歌曲名:",name)
        Downloader = wangyiyun()
        Downloader.work(id)

#已弃用 改用Download.py
# def download(music_id,name):
#     try:
#         url = 'http://music.163.com/song/media/outer/url?id=' + music_id + '.mp3'
#         path = r'D:\%s.mp3' % name   #下载文件存放路径
#         requests.urlretrieve(url, '{0}/{1}.mp3'.format(path, name))
#         requests
#         print("Success")
#     except:
#         print('Failed')#要会员才能“播放”的歌是不能下载的

#根据str搜索ID和名字
def getSong(name):
    searcher = search()
    #print('[Info]Got ID:'+id +'\n[Info]Got Name:'+ name)
    id,name = searcher.search_id(name)

    return id,name

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin =MyWindow()
    myWin.show()
    sys.exit(app.exec_())
