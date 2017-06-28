def get_most_played(file_name):
    file_list = []
    sold_list = []
    x = 0
    v = 0
    game_list = open(file_name, 'r')
    for line in game_list.readlines():
        fields = line.split('\t')
        file_list.append(fields)
    for i in range(len(file_list)):
            sold_list.append(file_list[x][1])
            x += 1
    for item in range(len(file_list)):
        if max(sold_list) in file_list[v]:
            return(file_list[v][0])
            break
        v += 1
