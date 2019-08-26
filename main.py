import time,sys,requests,threading
#PyQt GUI

from PyQt5.QtWidgets import QApplication, QMainWindow
from Form import *
#获取ID的API
from GetID import *
#下载音乐的API
class MyWindow(QMainWindow, Ui_Form):
    #初始化
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setFixedSize(265, 316)
        self.setupUi(self)
        self.directory = ''

    #重写父类中的按钮点击事件
    def Download_Button_click(self):
        #如果此时没有输入关键词
        if self.textEdit.toPlainText() == '':
            self.Console.append('[Error]请输入搜索关键词')
            return 0
        SearchName = self.textEdit.toPlainText()
        time.sleep(0.1)
        self.Console.append('[Info]正在搜索 -关键字: ' + SearchName)
        id, name = self.getSong(SearchName)
        # 如果搜索失败
        if id == None:
            self.Console.append('[Error]未搜索到相应歌曲，尝试更换关键词')
            return 0
        #搜索成功
        print("获得信息：\n  下载ID:",id,"\n   歌曲名:",name)
        time.sleep(0.1)
        self.Console.append('[Info]搜索到歌曲:'+ name)
        #如果还未设置路径（第一次执行下载）
        if self.directory == '':
            self.isNoPath = False
            self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
            self.Console.append('[Info]选定目录:' + self.directory)
        time.sleep(0.1)
        self.Console.append('[Info]开始下载:' + name)
        t = threading.Thread(target=self.download,args=(id,name,self.directory))
        t.setDaemon(False)
        t.start()

    def ChangeDownloadDir_Button_click(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.Console.append('[Info]选定目录:'+self.directory)
        print(self.directory)
        return self.directory

    # 下载music
    def download(self,music_id, music_name, directory):

        try:
            music_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % music_id
            print('开始下载 ' + music_name + ' 到 ' + directory + ' 目录')
            r = requests.get(music_url)
            path = directory + '\%s.mp3' % music_name  # 下载文件存放路径
            with open(path, 'wb') as f:
                f.write(r.content)
            time.sleep(1)
            print("成功下载" + music_name)
            self.Console.append('[Info]下载完成:' + music_name)
            return 0
        except Exception as e:
            print("错误:" + e)  # 要会员才能“播放”的歌是不能下载的
            self.Console.append('[Error]' + e)
            return 1


    #根据str搜索ID和名字
    def getSong(self,name):
        searcher = search()
        #print('[Info]Got ID:'+id +'\n[Info]Got Name:'+ name)
        id,name = searcher.search_id(name)

        return id,name

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin =MyWindow()
    myWin.show()
    sys.exit(app.exec_())
