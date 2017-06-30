from reports import*
import pprint
pprint.pprint(get_most_played("game_stat.txt"))
pprint.pprint(sum_sold("game_stat.txt"))
pprint.pprint(get_selling_avg("game_stat.txt"))
pprint.pprint(count_longest_title("game_stat.txt"))
pprint.pprint(get_date_avg("game_stat.txt"))
pprint.pprint(get_game("game_stat.txt", "Half-Life"))
