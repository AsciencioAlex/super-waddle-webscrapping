from bs4 import BeautifulSoup
# Using a stored HTML file
soup = BeautifulSoup(open("simple.html"))
# Entire HTML doc be passed
#soup = BeautifulSoup("<hmtl>data</html>")

#print soup
#print "==================================="
#print soup.prettify()

print "================================"
print soup.html.body.contents[1]
print "================================"

for tag in soup.find_all(True):
	print tag.name

print "=================================="

print soup.get_text('+')
print "=================================="
