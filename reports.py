# Report functions
def open_file(file_name="game_stat.txt"):
    content=""
    '''opens file and returns its content divided by line'''
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.readlines()
    except FileNotFoundError:
        print("File not found")
    except OSError:
        print("File Error")
    return(content)

def parse_content(file_name="game_stat.txt"):
    '''Takes content table(by line), transforms every line to dict and returns table of dict'''
    data_list=[]
    content=open_file(file_name)
    for entry in content:
        entry = entry.strip().split("\t")
        try:
            dict_entry={}
            dict_entry["title"]=entry[0]
            dict_entry["copies"]=entry[1]
            dict_entry["release"]=entry[2]
            dict_entry["genre"]=entry[3]
            dict_entry["publisher"]=entry[4]
            data_list.append(dict_entry)
        except IndexError:
            print("Wrong format")
        except ValueError:
            print("Wrong format")
    return(data_list)

def count_games(file_name="game_stat.txt"):
    content=parse_content(file_name)
    val = 0
    for i in content:
        val+=1
    return(val)

def decide(file_name, year):
    content=parse_content(file_name)
    for line in content:
        if int(year) == int(line["release"]):
            return True
    return False

def get_latest(file_name="game_stat.txt"):
    content=parse_content(file_name)
    latest_title=0
    entry=0
    latest=0
    for line in content:
        if latest < int(line["release"]):
            latest=int(line["release"])
            latest_title=entry
        entry+=1
    return content[latest_title]["title"]

def count_by_genre(file_name,genre):
    content=parse_content(file_name)
    count=0
    for line in content:
        if genre == line["genre"]:
            count+=1
    return count
def get_line_number_by_title(file_name, title):
    content=parse_content(file_name)
    line_nr=1
    for line in content:
        if title == line["title"]:
            return line_nr
        line_nr+=1
    return None

def sort_abc(file_name="game_stat.txt"):
    content=parse_content(file_name)
    name_table=[]
    for line in content:
        name_table.append(line["title"])
    name_table=sort_table(name_table)
    return name_table

def get_genres(file_name="game_stat.txt"):
    content=parse_content(file_name)
    genres=[]
    for line in content:
        if line["genre"] not in genres:
            genres.append(line["genre"])
    genres=sort_table(genres)
    return genres
            
def sort_table(content_table):
    for entry in content_table:
        for i in range(0, len(content_table)-1):
            if content_table[i+1] < content_table[i]:
                temp = content_table[i]
                content_table[i]=content_table[i+1]
                content_table[i+1]=temp
    return content_table

def when_was_top_sold_fps(file_name="game_stat.txt"):
    content=parse_content(file_name)
    entry_nr=0
    top_sold=0
    for line in content:
        if line["genre"]=="First-person shooter" and top_sold<float(line["copies"]):
            top_sold=float(line["copies"])
            top_entry_nr=entry_nr
        entry_nr+=1
    return int(content[top_entry_nr]["release"])