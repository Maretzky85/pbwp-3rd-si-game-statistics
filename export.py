from reports import *

content="{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(str(count_games()), str(decide("game_stat.txt",2012)), str(get_latest("game_stat.txt")), str(count_by_genre("game_stat.txt", "First-person shooter")), str(get_line_number_by_title("game_stat.txt", "Diablo III")), str(sort_abc("game_stat.txt")), str(get_genres("game_stat.txt")), str(when_was_top_sold_fps("game_stat.txt")))
try:
    with open("export.txt", 'w', encoding='utf-8') as f:
        f.write(content)
        f.close
        #print(content)
except FileNotFoundError:
        print("File not found")
except OSError:
        print("File Error")
