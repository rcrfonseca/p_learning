from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://prettyprinted.com')

# print (r.html.links)
print (r.html.absolute_links)
print ('\n')
print (r.html.find('.headline',first=True))
headline = r.html.find('.headline',first=True)
print ('\n')
print (headline.text)
print ('\n')

r = session.get('https://prettyprinted.com/p/the-flask-extensions-course')

print (r)

print (r.html.find('.course-section', first=True))
print ('\n')
flask_wtf_section = r.html.find('.course-section', first=True)

print (flask_wtf_section)
print ('\n')
print (flask_wtf_section.find('.item'))
items = flask_wtf_section.find('.item')
print ('\n')

for item in items:
	
	print (item.text)
	