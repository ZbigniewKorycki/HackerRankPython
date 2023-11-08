import operator

def person_lister(f):
    def inner(people):
        for person in people:
            person[2] = int(person[2])
        people.sort(key=operator.itemgetter(2))
        people_with_name_format = [f(person) for person in people]
        return people_with_name_format
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')