import re

html_code = [input() for _ in range(int(input()))]

html_code_joined = ''.join(html_code)

if "<!--" in html_code_joined and "-->" in html_code_joined:
    flag = True
else:
    flag = False

while flag:
    code_split = html_code_joined.split("<!--")
    code_before_comment = code_split[0]
    code_with_comment = code_split[1]
    try:
        code_after_comment = code_with_comment.split("-->")[1]
    except IndexError:
        code_after_comment = ''
    else:
        html_code_joined = code_before_comment + code_after_comment
    if "<!--" not in html_code_joined and "-->" not in html_code_joined:
        flag = False


matches = re.findall('<([a-zA-Z0-9]+)>*|\s([a-zA-Z0-9/-]+)="([^"]+)"', html_code_joined)
if matches:
    for match in matches:
        if match[0]:
            print(match[0])
        elif match[1] and match[2]:
            print(f"-> {match[1]} > {match[2]}")
