from statistics import mean


def get_stat_list(file_name):
    file_list = []
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        fields = line.split('\t')
        file_list.append(fields)
    return file_list


def get_list_sold(file_name):
    line_list = get_stat_list(file_name)
    sold_list = []
    nested = 0
    line_list = get_stat_list(file_name)
    for i in range(len(line_list)):
            sold_list.append(line_list[nested][1])
            nested += 1
    return sold_list


def get_most_played(file_name):
    nested = 0
    line_list = get_stat_list(file_name)
    sold = get_list_sold(file_name)
    sold = sorted(sold, key=float, reverse=True)
    for i in range(len(sold)):
        if sold[0] in line_list[nested]:
            return(line_list[nested][0])
        nested += 1


def sum_sold(file_name):
    sold = get_list_sold(file_name)
    sold = [float(i) for i in sold]
    return (sum(sold))


def get_selling_avg(file_name):
    line_list = get_stat_list(file_name)
    solds = sum_sold(file_name)
    return(solds/len(line_list))


def count_longest_title(file_name):
    nested = 0
    line_list = get_stat_list(file_name)
    title_list = []
    for i in range(len(line_list)):
            title_list.append(line_list[nested][0])
            nested += 1
    return(len(max(title_list, key=len)))


def get_date_avg(file_name):
    nested = 0
    date_list = []
    line_list = get_stat_list(file_name)
    for i in range(len(line_list)):
        date_list.append(line_list[nested][2])
        nested += 1
    date_list = [float(i) for i in date_list]
    return round(mean(date_list))


def get_game(file_name, title):
    nested = 0
    line_list = get_stat_list(file_name)
    for i in range(len(line_list)):
        if title in line_list[nested]:
            line_list[nested][1] = float(line_list[nested][1])
            line_list[nested][2] = int(line_list[nested][2])
            line_list[nested][4] = line_list[nested][4].rstrip('\n')
            return line_list[nested]
        nested += 1

get_game("game_stat.txt","Minecraft")
