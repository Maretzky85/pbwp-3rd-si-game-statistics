from reports import *

def ask_q():
    file_name="game_stat.txt"
    var=input("What do You need?\n0 - Change File name(default:game_stat.txt)\n1 - Count games in file\n2 - Latest game in file\n3 - Count games by Genre\n4 - Title line number in file\n5 - Get genres in file\n6 - Top sold fps\nAny other - quit\n")
    return file_name, var

def change_filename():
    file_name=input("Enter file name:")
    if check_file(file_name)==False:
        print("File not found")
        return ("game_stat.txt")
    return file_name

def check_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return True
    except FileNotFoundError:
        return False
    

def main():
    while True:
        file_name, choise=ask_q()
        try:
            choise=int(choise)
        except ValueError:
            break
        if choise==0:
            file_name=change_filename()
        elif choise == 1:
            print(count_games(file_name))
        elif choise == 2:
            print(get_latest(file_name))
        elif choise == 3:
            genre=input("What genre?\n")
            print(count_by_genre(file_name, genre))
        elif choise == 4:
            name=input("Game title?\n")
            print(get_line_number_by_title(file_name, name))
        elif choise == 5:
            print(get_genres(file_name))
        elif choise == 6:
            print(when_was_top_sold_fps())
main()