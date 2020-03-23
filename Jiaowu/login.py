from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p><b>The Dormouse's story</b></p>

<p>Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie">Elsie</a>,
<a href="http://example.com/lacie">Lacie</a> and
<a href="http://example.com/tillie">Tillie</a>;
and they lived at the bottom of a well.</p>

<p>...</p>
"""
soup=BeautifulSoup(html_doc,'lxml')
print(soup.html.body.p.b)
