import re


name_re = re.compile(' ([A-Z][A-Za-z]+\s+[A-Z][A-Za-z]+|[A-Z][A-Za-z]+)')


result = name_re.findall(practice)
print(result)


def find_names(txt_msg):
    names = name_re.findall(txt_msg)
    print(names)
    return names


def full_excel()
    pass



if __name__=="__main__":
    practice = 'Daniel Diaz    Samantha went to work   Daniel Armentor came over.'
