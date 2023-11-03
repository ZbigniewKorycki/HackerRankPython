import re

regex_pattern = r"^(M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V|V?I{0,3}))$"


roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                  "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C",
                  "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M", "MM",
                  "MMM", "MMCMXCIX"]

invalid_roman_numerals = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMMM",
                         "XXXXX", "LXL", "CMC", "IXI", "XCX", "CDC", "LD", "VVV",
                         "IIIL", "IL", "IC", "IM", "XM", "XD", "XLC", "XCC", "DDC",
                         "DM", "LM", "XM", "IIX", "XXC", "CCD", "MCMC", "VIV", "VC",
                         "DIL", "LDL", "MMMCMCMC", "MMMMMCMXCIX", "MMMMMCMXC"]

for number in roman_numerals:
    print(number, end=": ")
    print(str(bool(re.match(regex_pattern, number))))

print("---------------------------")

for number in invalid_roman_numerals:
    print(number, end=": ")
    print(str(bool(re.match(regex_pattern, number))))


