import re

#print(re.search("tara","tcs "))

news="TCS is good."
news = news.lower()
#print(news)
tokens = ["tcs","tata consultancy services"] 
for i in tokens:
	print(i, news )
	if re.search(i, news):
		print("works fine 1")
