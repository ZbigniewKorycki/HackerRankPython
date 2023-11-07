import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    if len(elem) > 0:
        if maxdepth < 2 + level:
            maxdepth = 2 + level
        for sub_one_down in elem:
            if len(sub_one_down) > 0:
                if maxdepth < 3 + level:
                    maxdepth = 3 + level
                for sub_two_down in sub_one_down:
                    if len(sub_two_down) > 0:
                        if maxdepth < 4 + level:
                            maxdepth = 4 + level
                        for sub_three_down in sub_two_down:
                            if len(sub_three_down) > 0:
                                if maxdepth < 5 + level:
                                    maxdepth = 5 + level
                                for sub_four_down in sub_three_down:
                                    if len(sub_four_down) > 0:
                                        if maxdepth < 6 + level:
                                            maxdepth = 6 + level
                                    else:
                                        continue
                            else:
                                continue
                    else:
                        continue
            else:
                continue


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)