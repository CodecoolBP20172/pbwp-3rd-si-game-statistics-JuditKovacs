def count_games(file_name):
    number_of_lines = 0
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        number_of_lines += 1
    return(number_of_lines)
    game_list.close()


def get_stat_list(file_name):
    file_list = []
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        fields = line.split('\t')
        file_list.append(fields)
    return file_list
    game_list.close()

def years(file_name):
    line_list = get_stat_list(file_name)
    year_list = []
    nested_list = 0
    for i in range(len(line_list)):
            year_list.append(line_list[nested_list][2])
            nested_list += 1
    return year_list



def decide(file_name, year):
    list_of_years = years(file_name)
    list_of_years = [int(i) for i in list_of_years]
    if year in list_of_years:
        return True



def get_latest(file_name):
    list_of_years = years(file_name)
    line_list = get_stat_list(file_name)
    nested_list = 0
    for item in range(len(line_list)):
        if max(list_of_years) in line_list[nested_list]:
            return(line_list[nested_list][0])
            break
        nested_list += 1



def count_by_genre(file_name, genre):
    line_list = get_stat_list(file_name)
    nested_list = 0
    number = 0
    for nested_list in range(len(line_list)):
        if genre in line_list[nested_list]:
            number += 1
    nested_list += 1
    return(number)


def get_line_number_by_title(file_name, title):
    game_list = open(file_name, 'r')
    l_n_title = 0
    for line in game_list.readlines():
        l_n_title += 1
        if title in line:
            return(l_n_title)
            break
        try:
            title in line
            if l_n_title > count_games(file_name):
                raise ValueError
        except ValueError as err:
            return "There in no game with this title"
    game_list.close()
