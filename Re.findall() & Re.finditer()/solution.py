import re

consonants_upper = 'QWRTYPSDFGHJKLZXCVBNM'
consonants_lower = 'qwrtypsdfghjklzxcvbnm'

vowels_upper = 'AEIOU'
vowels_lower = 'aeiou'

match = re.findall(r'(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}[AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}))', input())

if match:
    for elements in match:
        print(elements[1:-1])
else:
    print(-1)