import pprint
from reports import*
pprint.pprint(count_games("game_stat.txt"))
pprint.pprint(decide("game_stat.txt", 2000))
pprint.pprint(get_latest("game_stat.txt"))
pprint.pprint(count_by_genre("game_stat.txt", 'Simulation'))
pprint.pprint(get_line_number_by_title("game_stat.txt", "The Sims 2"))
