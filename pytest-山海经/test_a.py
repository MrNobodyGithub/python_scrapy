import requests
import json
import urllib
from lxml import etree

def downImage(path): 

	url=path
	# "http://image109.360doc.com/DownloadImg/2018/05/0723/132411022_3_20180507112810113"
	headers={"Referer":"http://www.360doc.com/content/18/0507/23/6152050_752016689.shtml","User-Agent":"Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_6)AppleWebKit/537.36 (KHTML,like Gecko)Chrome/70.0.3538.110 Safari/537.36",}

	response=requests.get(url,headers=headers).content
	# print(response)

	name = path.split('/')[-1][10:12]
	name = name.replace('_','')
	name = str(int(name) -1)

	with open('/Users/shuzishijian/Desktop/pytest/img/'+name+'.png', 'wb') as f:
		f.write(response)
 
def getjson():
	url = "/Users/shuzishijian/Desktop/pytest/items.json"
	f = open(url, encoding='utf-8')
	setting = json.load(f)
	imageList = []
	for dic in setting:
		imageList.append(dic["img"]);
	return imageList;
list = getjson()
num = 0;
for imgurl in list:
	# print(imgurl);
	print('downloading for' + str(num + 1))
	downImage(imgurl)
	num = num + 1;

print('downloading all')





# def getSogouImag(category,length,path):
# 	n = length
# 	cate = category
# 	url =  'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n)
# 	header = {
# 	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# 	}
# 	imgs = requests.get(url)
#     # imgs = requests.get(url,headers=header)

#     jd = json.loads(imgs.text)
#     jd = jd['all_items']
#     imgs_url = []
#     for j in jd:
#     	imgs_url.append(j['pic_url'])
#         # imgs_url.append(j['bthumbUrl'])
#         m = 0
#         for img_url in imgs_url: 
#         	print('***** '+str(m)+'.jpg *****'+' Downloading...' + img_url);
#         	urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
#         	m = m + 1
#         	print('Download complete!')

# getSogouImag('壁纸',1000,'/Users/shuzishijian/Desktop/asdf/z')


# testa('/Users/shuzishijian/Desktop/asdf/z')