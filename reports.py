def count_games(file_name):
    number_of_lines = 0
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        number_of_lines += 1
    return(number_of_lines)
    game_list.close()


def decide(file_name, year):
    file_list = []
    nested_list = 0
    year_list = []
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        fields = line.split('\t')
        file_list.append(fields)
    for i in range(len(file_list)):
            year_list.append(file_list[nested_list][2])
            nested_list += 1
            year_list = [int(i) for i in year_list]
            if year in year_list:
                return True
    game_list.close()


def get_latest(file_name):
    file_list = []
    year_list = []
    x = 0
    v = 0
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        fields = line.split('\t')
        file_list.append(fields)
    for i in range(len(file_list)):
            year_list.append(file_list[x][2])
            x += 1
    for item in range(len(file_list)):
        if max(year_list) in file_list[v]:
            return(file_list[v][0])
            break
        v += 1
    game_list.close()


def count_by_genre(file_name, genre):
    file_list = []
    nested_list = 0
    number = 0
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        fields = line.split('\t')
        file_list.append(fields)
    for nested_list in range(len(file_list)):
        if genre in file_list[nested_list]:
            number += 1
    nested_list += 1
    return(number)
    game_list.close()


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
