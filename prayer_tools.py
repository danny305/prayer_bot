import re
from glob import glob
from collections import namedtuple
from prayer_bot.prayer_sqlalchemy_db import create_csv,create_excel

name_re = re.compile(' ([A-Z][A-Za-z]+\s+[A-Z][A-Za-z]+|[A-Z][A-Za-z]+)')
file_format = re.compile('([0-9]{2})-([0-9]{2})-.{3}([0-9]{2})')

# result = name_re.findall(practice)
# print(result)


def find_names(txt_msg):
    names = name_re.findall(txt_msg)
    print(names)
    return names


def full_excel():
    pass

def find_most_recent(query='*.csv',create=False):
    """Finds the most recent excel or csv file that is title with the %m-%d-%y_%H:%M."""
    if create == False:
        all_files = tuple(glob(query))
        sorter = namedtuple('Sorter',['month','day','hour','index'])
        winner = sorter(0,0,0,0)

        for index, x in enumerate(all_files):
            month, day, hour = file_format.split(x)[1:-1]   #This is a re split not str
            if int(month) > winner.month:
                winner = winner._replace(month=int(month),day=int(day),hour=int(hour),index=index)
            elif int(day) > winner.day:
                winner = winner._replace(month=int(month), day=int(day), hour=int(hour),index=index)
            elif int(hour) >= winner.hour:
                winner = winner._replace(month=int(month), day=int(day), hour=int(hour),index=index)

        print(all_files[winner.index])
        return all_files[winner.index]

    else:
        if 'csv' in query:
            print('creating CSV')
            create_csv()
            return find_most_recent(query='*.csv', create=False)
        elif 'xlsx' in query:
            create_excel()
            return find_most_recent(query='*xlsx', create=False)






if __name__=="__main__":
    practice = 'Daniel Diaz    Samantha went to work   Daniel Armentor came over.'
    find_most_recent()
