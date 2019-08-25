import requests,os,time,sys,re
from scrapy.selector import Selector

class wangyiyun():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/'}
        self.main_url='http://music.163.com/'
        self.session = requests.Session()
        self.session.headers=self.headers

    def get_songurls(self,playlist):
        url=self.main_url+'playlist?id=%d'% playlist
        re= self.session.get(url)   #直接用session进入网页，懒得构造了
        sel=Selector(text=re.text)   #用scrapy的Selector，懒得用BS4了
        songurls=sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        return songurls   #所有歌曲组成的list
        ##['/song?id=64006', '/song?id=63959', '/song?id=25642714', '/song?id=63914', '/song?id=4878122', '/song?id=63650']

    def get_songinfo(self,songurl):

        url=self.main_url+songurl
        re=self.session.get(url)
        sel=Selector(text=re.text)
        song_id = url.split('=')[1]
        song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
        singer= '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
        songname=singer+'-'+song_name
        return str(song_id),songname

    def download_song(self, songurl, dir_path):

        song_id, songname = self.get_songinfo(songurl)  # 根据歌曲url得出ID、歌名
        song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%song_id
        path = dir_path + os.sep + songname + '.mp3'  # 文件路径
        requests.urlretrieve(song_url, path)  # 下载文件

    def work(self, playlist):
        dir_path = r'D:\MusicDownloader'  # 下载路径
        songurls = self.get_songurls(playlist)  # 输入歌单编号，得到歌单所有歌曲的url
        for songurl in songurls:
            self.download_song(songurl, dir_path)  # 下载歌曲
