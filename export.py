from reports import *
title = input("Enter game name for report and press enter: ")
genre = input("enter genre for report: ")
year = input("enter Year for report: ")
content="{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(str(decide("game_stat.txt", year)),\
                                                str(count_games()),\
                                                str(decide("game_stat.txt",year)),\
                                                str(get_latest("game_stat.txt")),\
                                                str(count_by_genre("game_stat.txt", genre)),\
                                                str(get_line_number_by_title("game_stat.txt", title)),\
                                                ", ".join(get_genres("game_stat.txt")),\
                                                str(when_was_top_sold_fps("game_stat.txt")),\
                                                str(", ".join(sort_abc("game_stat.txt"))))
try:
        with open("export.txt", 'w', encoding='utf-8') as f:
                f.write(content)
                f.close
except OSError:
        print("File Error")
