from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            [print(comment_line) for comment_line in data.split('\n')]
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ""

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
