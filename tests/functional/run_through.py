from splinter import Browser

browser = Browser()
url = 'http://localhost:4000'
browser.visit(url)
assert browser.is_text_present('hello world')
browser.quit()