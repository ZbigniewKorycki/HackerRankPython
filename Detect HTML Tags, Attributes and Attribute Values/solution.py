import re

def find_match(html_code):
    matches = re.findall('<([a-zA-Z0-9]+)>*|\s([a-zA-Z0-9/-]+)="([^"]+)"', html_code)
    if matches:
        for match in matches:
            if match[0]:
                print(match[0])
            elif match[1] and match[2]:
                print(f"-> {match[1]} > {match[2]}")


html_code = [input() for _ in range(int(input()))]
html_code_joined = ''.join(html_code)

text_without_comments = re.sub(r'<!--.*?-->', '', html_code_joined)
find_match(text_without_comments)