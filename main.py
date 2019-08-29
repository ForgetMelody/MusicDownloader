import time,sys,threading
from pprint import pprint
#PyQt GUI
from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.sip
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
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
                }#伪装 防反爬虫

    #重写父类中的按钮点击事件
    def Download_Button_click(self):
        #如果此时没有输入关键词
        if self.textEdit.toPlainText() == '':
            self.Console.append('[Error]请输入搜索关键词')
            return 0
        SearchName = self.textEdit.toPlainText()
        time.sleep(0.1)
        id, name = self.getSong(SearchName)
        # 如果搜索失败
        if id == None:
            self.outPutMessageToConsole('[Error]未搜索到相应歌曲，尝试更换关键词')
            return 0
        #搜索成功
        print("获得信息：\n   下载ID:",id,"\n   歌曲名:",name)
        time.sleep(0.1)
        self.outPutMessageToConsole('[Info]搜索到歌曲:'+ name)
        #如果还未设置路径（第一次执行下载）
        if self.directory == '':
            self.directory = self.ChangeDownloadDir_Button_click()
        time.sleep(0.1)
        self.outPutMessageToConsole('[Info]开始下载:' + name)
        downloadSong = threading.Thread(target=self.downloadSong, args=(id, name, self.directory))
        downloadSong.setDaemon(False)
        downloadSong.start()
        if self.checkBox.isChecked():#勾选了下载歌词
            print('开始下载歌词：' + name)
            downloadLyric = threading.Thread(target=self.downloadLyric, args=(id, name, self.directory))
            downloadLyric.setDaemon(False)
            downloadLyric.start()


    def ChangeDownloadDir_Button_click(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.outPutMessageToConsole('[Info]选定目录:'+self.directory)
        print(self.directory)
        return self.directory

    # 下载music
    def downloadSong(self, music_id, music_name, directory):

        try:
            music_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % music_id

            print('开始下载' + music_name + ' 到 ' + directory + ' 目录')
            r = requests.get(url=music_url,headers=self.headers)
            pprint(r)#Response [200]即成功
            path = directory + '\%s.mp3' % music_name  # 下载文件存放路径
            with open(path, 'wb') as f:
                f.write(r.content)
            time.sleep(1)
            print("歌曲下载完成:" + music_name)
            self.outPutMessageToConsole('[Info]歌曲下载完成:' + music_name)
            return 0
        except Exception as e:
            print(e)  # 要会员才能“播放”的歌是不能下载的
            self.outPutMessageToConsole("[Error]请使用控制台查看错误")
            return 1

    #下载歌词
    def downloadLyric(self,music_id,music_name,directory):
        try:
            lyric_url = 'http://music.163.com/api/song/lyric?id=%s&lv=1&kv=1&tv=-1' % music_id
            self.outPutMessageToConsole('[Info]开始下载歌词:' + music_name)
            r = requests.get(url=lyric_url,headers=self.headers)
            json_obj = r.text
            j = json.loads(json_obj)
            lyric = j['lrc']['lyric']
            path = directory + '\%s.txt' % music_name #下载文件存放路径
            with open(path,'w') as f:
                f.write(lyric)
            time.sleep(1)
            print('成功下载歌词:' + music_name)
            self.outPutMessageToConsole('[Info]歌词下载完成:' + music_name)
        except Exception as e:
            print(e)


    #根据str搜索ID和名字
    def getSong(self,name):
        searcher = search()
        #print('[Info]Got ID:'+id +'\n[Info]Got Name:'+ name)
        self.outPutMessageToConsole('[Info]正在搜索关键字: ' + name)
        id,name = searcher.search_id(name)

        return id,name

    def outPutMessageToConsole(self,str):
        self.Console.append(str)
        self.Console.moveCursor(self.Console.textCursor().End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin =MyWindow()
    myWin.show()
    sys.exit(app.exec_())
