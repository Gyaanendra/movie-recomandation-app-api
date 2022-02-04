import csv


with open("movies.csv","r") as f:
    f_reader  = csv.reader(f)
    data = list(f_reader)
    headers = data[0]
    all_movies  = data[1:]
    
    
headers.append("links")

with open("final.csv","a+") as r:
    file_write = csv.writer(r)
    file_write.writerow(headers)
    
with open("links.csv","r") as l:
    l_reader = csv.reader(l)
    data = list(l_reader)
    poster_link = data[1:]
    

for i in all_movies:
    poster = any(i[8] in movies_link for movies_link in poster_link)
    if poster :
        for g in poster_link:
            if i[8] == g[0]:
                i.append(g[1])
                if len(i) == 28:
                    with open("final.csv","a+") as k:
                        k_write = csv.writer(k)
                        k_write.writerow(i)
                        
                        
                    