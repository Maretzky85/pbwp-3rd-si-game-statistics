
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

def sort_table(content_table):
    for entry in content_table:
        for i in range(0, len(content_table)-1):
            if content_table[i+1] < content_table[i]:
                temp = content_table[i]
                content_table[i]=content_table[i+1]
                content_table[i+1]=temp
    return content_table

def get_most_played(file_name):
    content=parse_content(file_name)
    latest_title=0
    entry=0
    latest=0
    for line in content:
        if latest < float(line["copies"]):
            latest=float(line["copies"])
            latest_title=entry
        entry+=1
    return content[latest_title]["title"]

def sum_sold(file_name):
    content=parse_content(file_name)
    sum=0
    for line in content:
        sum+=float(line["copies"])
    return sum

def get_selling_avg(file_name):
    content=parse_content(file_name)
    sum=0
    divider=0
    for line in content:
        sum+=float(line["copies"])
        divider+=1
    return sum/divider

def count_longest_title(file_name):
    content=parse_content(file_name)
    longest_title=0
    for line in content:
        if longest_title<len(line["title"]):
            longest_title=len(line["title"])
    return longest_title

def get_date_avg(file_name):
    content=parse_content(file_name)
    sum=0
    divider=0
    for line in content:
        sum+=float(line["release"])
        divider+=1
    return int(round(sum/divider,0))

def get_game(file_name, title):
    content=parse_content(file_name)
    properties_table=[]
    for line in content:
        if title==line["title"]:
            for entry in line:
                prop=line[entry]
                try:
                    prop=int(prop)
                except ValueError:
                    try:
                        prop=float(prop)
                    except ValueError:
                        prop=str(prop)    
                properties_table.append(prop)
    return properties_table



print(get_most_played("game_stat.txt"))
print(sum_sold("game_stat.txt"))
print(get_selling_avg("game_stat.txt"))
print(count_longest_title("game_stat.txt"))
print(get_date_avg("game_stat.txt"))
print(get_game("game_stat.txt", "Diablo III"))