import re

for _ in range(int(input())):
    line_of_html_code = input()
    if "<!--" in line_of_html_code:
        comment_begin = line_of_html_code.split("<!--")
        line_of_html_code = comment_begin[0]
    if "-->" in line_of_html_code:
        comment_end = line_of_html_code.split("-->")
        line_of_html_code = comment_end[1]
    matches = re.findall('<([a-zA-Z0-9]+)>*|\s([a-zA-Z0-9/]+)="([^"]+)"', line_of_html_code)
    if matches:
        for match in matches:
            if match[0]:
                print(match[0])
            elif match[1] and match[2]:
                print(f"-> {match[1]} > {match[2]}")
