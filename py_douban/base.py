
from retrying import retry
import requests
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

@retry(stop_max_attempt_number=3)


def _parse_url(url):
	# print('*'*10)
	response = requests.get(url,headers=headers,timeout=5)
	return response.content.decode()
def parse_url(url):
	try:
		html_str = _parse_url(url)
	except:
		html_str = None
	return html_str

if __name__ == '__main__':
	url = "http://www.baidu.com"
	print(parse_url(url))




