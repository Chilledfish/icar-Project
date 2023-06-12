from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from lxml import html
import urllib3
from http import cookiejar

#website = urlopen("https://qm.konesonline.co.il/Account/Login")



payload = {
	"UserName": "editor@kones.co.il",
	"Password": "editor123",
	#"__RequestVerificationToken": "SYA9W5HyMenQ1RdToRYZ1KxaekLQvgaMAtIMXGMEvntuiV50-U1ZEQHJzntvS6GpYYptYeN6EwT0ODcRAr5mhQERPGFnTMhdWH_CUkRqTmTHntw95X3lPIVMcDM76DC7xTnBPT19MtgRxba4n1FMpQ2"
}
session_requests = requests.session()
login_url = "https://qm.konesonline.co.il/Account/Login"
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

result = session_requests.post(
	login_url,
	data=payload,
	headers=dict(referer=login_url)
)



b=5



'''cj = cookiejar.CookieJar()
br = cookiejar.MozillaCookieJar()

br.open("https://qm.konesonline.co.il/Account/Login")

br.select_form(nr=0)
br.form['username'] = "editor@kones.co.il"
br.form['password'] = "editor123"
br.submit()
moo = br.response().read()'''
b=5