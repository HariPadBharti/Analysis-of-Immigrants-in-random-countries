def read_data(fname):
    # read in the data from filename fname
    # return a single object
    import csv
    data = []
    with open(fname, "rU") as f:
        reader = csv.reader(f)
        line = f.readline();
        line = f.readline();                 #returns the data , print(data) can be used to read data
        line = f.readline();     
        line = f.readline();
        for row in reader:
            data.append(row)
    return data

def num_countries(data):
    # return the total number of unique countries
    c=set()
    for i in range(len(data)):      #since sets always holds unique elements, we can get the exact no of unique countries.
        c.add(data[i][1])
    a=len(c)
    return a

def origins(data, country):
    # given a country name, return the countries that the persons of concern originated from
    e = set()
    for i in range(len(data)):
        if data[i][1] == country:
            e.add(data[i][2])  #here the second column represents origin and set helps to get non repeated unique countries.
    return e
    return []

def max_people(data, country):
    # given a country name, return the year that the maximum number of persons of a concern were in that country and how many were there
    n = {}
    for row in data:
        if row[1] == country:
            year=row[0]
            p=row[10]
    #for i in range(len(data)):
        #if data[i][1]== country:
            #year=data[i][0] //This can't work because of one to one unique comparison
            #p=data[i][0]
            if p == '*':
                p=4
            if year not in n:
                n[year] = int(p) #since is added as a string
            else:
                n[year] = n[year] + int(p)             
    max_y = max(n, key=n.get)
    return (max_y, n[max_y]) #max_y represents year of maximum_immegrants_population
    return (1900, 0)

def calc_2014range(data, country):
    # given a country name, return the possible minimum and maximum of the number of persons of concern in that country in 2014
    max_v =0
    min_v=0
    #for i in range(len(data)):
        #if data[i][1]== country:
            #year=data[i][0] //This can't work because of one to one unique comparison
            #p=data[i][0]
    for row in data:
        if row[1] == country:
            year=row[0]
            p=row[10]
            if (year=='2014'):
                 if p == '*':
                        max_add =4     #here population is added with 4 as max while 1 as min value. 
                        min_add =1
                        max_v= max_add+int(max_v)
                        min_v=min_add+int(min_v)
                 else:
                    max_v += int(p)    #here we evaluate possible max population and min respectively to give the required range.
                    min_v += int(p)
    return (min_v, max_v)
    return (0,100)

def run(fname):
    data = read_data(fname)
    print("Number of unique countries/territories:", num_countries(data))
    for country in ["Turks and Caicos Islands", "Qatar"]:
        result = origins(data, country)
        print("Origin of refugees in {}:".format(country),
              ', '.join(sorted(result)))
    for country in ["Greece", "United States of America"]:
        country_max = max_people(data, country)
        print ("{} | Year of Maximum: {}, Number: {}".format(country,
                                                             country_max[0],
                                                             country_max[1]))
    for country in ["France", "Australia"]:
        r = calc_2014range(data, country)
        print("2014 Range for {}: {}-{}".format(country, r[0], r[1]))
              
if __name__ == '__main__':
    run("unhcr_popstats_export_persons_of_concern_all_data.csv")
