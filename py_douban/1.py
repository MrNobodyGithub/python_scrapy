from base import parse_url
import json
import requests




class DoubanSpilder():
	def __init__(self):
		self.temp_url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E8%A7%86%E5%89%A7,%E7%94%B5%E8%A7%86%E5%89%A7&start={}"

	def get_content_list(self,url): 
		dict_data = json.loads(url)
		content_list = dict_data["data"]
		return content_list 
	def save_content_list(self,content_list):
		with open("doubana.json","a",encoding="utf-8") as f:
			for content in content_list:
				f.write(json.dumps(content,ensure_ascii=False))
				# f.write("\n")
				# f.write(",")
			f.write('\n')
	def run(self):
		right = True
		stand = 200
		num = stand
		while right:
			print("*"*10+str(num/stand)+"*"*10)
			url = self.temp_url.format(num)
			if num<300:
				print(url)

			html_str = parse_url(url)
			content_list = self.get_content_list(html_str)
			lista = list(content_list)
			# print(content_list)
			# print(lista)

			print(len(lista))
			if len(lista) == 0:
				right = False
			# elif num > 10:
			# 	right = False
			else:
				self.save_content_list(content_list)
				num += stand

		

DoubanSpilder().run()