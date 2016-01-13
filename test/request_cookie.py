import requests

s = requests.session()
proxies = {'http': 'http://127.0.0.1:8080'}

headers = {'content-type': 'application/json','User-agent':'Opera/9.23','referer':'http://bgp.he.net'}

s.get("http://bgp.he.net/dns/www.95516.com",headers=headers,allow_redirects=True)
#s.get("http://bgp.he.net/cc",headers=headers)
#s.get("http://bgp.he.net/jf",headers=headers)
#s.get("http://bgp.he.net/jc",headers=headers)
#s.get("http://bgp.he.net/cr",headers=headers)
resp = s.get("http://bgp.he.net/dns/www.95516.com",headers=headers,proxies=proxies).text
print resp
