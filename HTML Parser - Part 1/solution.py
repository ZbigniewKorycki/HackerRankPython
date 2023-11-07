import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attribute in attrs:
                print(f"-> {attribute[0]} > {attribute[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for attribute in attrs:
                print(f"-> {attribute[0]} > {attribute[1]}")


html_code = [input() for _ in range(int(input()))]
html_code_joined = ''.join(html_code)

parser = MyHTMLParser()
html_code_without_comments = re.sub(r'<!--.*?-->', '', html_code_joined)
parser.feed(html_code_without_comments)
