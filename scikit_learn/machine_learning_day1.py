

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text  import CountVectorizer
from sklearn.feature_extraction.text  import TfidfVectorizer
import jieba

def irisDemo(): 
	iris = load_iris()
	# print("鸢尾花数据集:\n",iris)
	# print("查看数据集描述:\n",iris['DESCR'])
	print("查看特征值:\n",iris.data,iris.data.shape)
	# print("查看特征值:\n",iris.data.shape)
	# print("查看目标值 行列数:\n",iris.target)

	# print("查看特征名称:\n",iris.feature_names)
	# print("查看目标名称:\n",iris.target_names)

	x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

	print("x_train:\n",x_train,x_train.shape)
	print("x_test:\n",x_test,x_test.shape)
	print("y_train:\n",y_train,y_train.shape)
	print("y_test:\n",y_test,y_test.shape)


# 字典特征抽取
def dict_demo():
	data=[{'city':'北京','temperature':100},{'city':'上海','temperature':60},{'city':'深圳','temperature':30}]
	# 1 实例化一个转换器类
	transfer = DictVectorizer(sparse=False)

	# 2 调用 fit_transform()
	data_new = transfer.fit_transform(data)
	print("data_new\n",data_new,type(data_new))
	print("特征名字\n",transfer.get_feature_names())

def text_demo(): #文本特征抽取
	data = ["lift is short, i like python","life is too long,i dislike python"]
	transfer = CountVectorizer()
	data_new = transfer.fit_transform(data)
	print("data_new:\n",data_new.toarray(),type(data_new))

	print("特征名字\n",transfer.get_feature_names())
def text_chinese_demo():
	data = ["我 爱 北京 天安门","天安门 上 太阳 升"]
	transfer = CountVectorizer()
	data_new = transfer.fit_transform(data)
	print("data_new\n",data_new.toarray(),type(data_new))
	print("特征名字\n",transfer.get_feature_names())

def cut_word(text):
	 # 中文分词
	text = " ".join(list(jieba.cut(text)))
	return text;

def text_chinese2_demo():
	data = ["一种还是一种今天很残酷,明天跟残酷,后天很美好,但绝对大部分是死在明天晚上,所以每个人不要放弃今天","我们看到的从很远星系来的光是在几百万年之前发出的,这样当我们看到宇宙时,我们看到的是他的过去","如果只用一种方式了解某样事物,就不会真正的了解它.了解事物真正含义的秘密取决于如何将其与我们所了解的事物相关联"]

	data_list = []
	for sent in data:
		data_list.append(cut_word(sent))
	print(data_list)
	transfer = CountVectorizer(stop_words=["一种"])
	data_new = transfer.fit_transform(data_list)
	print("data_new\n",data_new.toarray(),type(data_new))
	print("特征名字\n",transfer.get_feature_names())

def tfidf_demo():
	# 文本特征提取
	data = ["一种还是一种今天很残酷,明天跟残酷,后天很美好,但绝对大部分是死在明天晚上,所以每个人不要放弃今天","我们看到的从很远星系来的光是在几百万年之前发出的,这样当我们看到宇宙时,我们看到的是他的过去","如果只用一种方式了解某样事物,就不会真正的了解它.了解事物真正含义的秘密取决于如何将其与我们所了解的事物相关联"]

	data_list = []
	for sent in data:
		data_list.append(cut_word(sent))
	print(data_list)
	transfer = TfidfVectorizer(stop_words=["一种"])
	data_new = transfer.fit_transform(data_list)
	print("data_new\n",data_new.toarray(),type(data_new),data_new.shape)
	print("特征名字\n",transfer.get_feature_names())
	return None
if __name__ == "__main__":
	# irisDemo()
	# dict_demo()
	# text_demo()
	# text_chinese_demo()
	# cut_word("我爱北京天安门")
	# text_chinese2_demo()
	tfidf_demo();
























