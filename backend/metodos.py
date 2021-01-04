import sys
sys.path.append('')

from backend.log import log


def marketplaces():
    title = 'marketplaces'
    marketplace_list = read_files(title)
    log(title)
    return marketplace_list


def categories():
    title = 'categories'
    category_list = read_files(title)
    category_list.append(sub_categories())
    log(title)
    return category_list


def sub_categories():
    title = 'sub_categories'
    sub_category_list = read_files(title)
    log(title)
    return sub_category_list


def read_files(title):
    file = open('backend/lists.txt', 'r')

    for line in file:
        list_ = line.strip().split(';')

        if list_[0] == title:
            list_.remove(title)
            file.close()
            return list_

        elif list_[0] == title:
            list_.remove(title)
            file.close()
            return list_

        elif list_[0] == title:
            list_.remove(title)
            file.close()
            return list_


def new_marketplaces(mkt:str) -> None:

    file = open('backend/lists.txt', 'r+')
    temp_file = file.readlines()
    file.seek(0)
    for line in temp_file:
        if 'marketplaces' in line:
            line.strip()
            mkt_line = line + ';' + mkt
        if 'marketplaces' not in line:
            file.write(line)
    file.write(mkt_line)
    file.truncate()
    file.close()

    log(f'marketplace {mkt} created')
