import re
from glob import glob
from collections import namedtuple

name_re = re.compile(' ([A-Z][A-Za-z]+\s+[A-Z][A-Za-z]+|[A-Z][A-Za-z]+)')


# result = name_re.findall(practice)
# print(result)


def find_names(txt_msg):
    names = name_re.findall(txt_msg)
    print(names)
    return names


def full_excel():
    pass

def find_most_recent_excel():
    all_excel = glob('*xlsx')
    sorter = namedtuple('Sorter',['month','day','hour','index'])
    winner = sorter(0,0,0,0)

    for index, x in enumerate(all_excel):
        month, day, hour = re.split('([0-9]{2})-([0-9]{2})-.{3}([0-9]{2})',x)[1:-1]
        if int(month) > winner.month:
            winner = winner._replace(month=int(month),day=int(day),hour=int(hour),index=index)
        elif int(day) > winner.day:
            winner = winner._replace(month=int(month), day=int(day), hour=int(hour),index=index)
        elif int(hour) > winner.hour:
            winner = winner._replace(month=int(month), day=int(day), hour=int(hour),index=index)

    return all_excel[winner.index]



if __name__=="__main__":
    practice = 'Daniel Diaz    Samantha went to work   Daniel Armentor came over.'
    find_most_recent_excel()
