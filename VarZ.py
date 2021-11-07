import csv
                    
with open('userReviews.csv', encoding='utf-8-sig') as reviews:
  reader = csv.DictReader(reviews,delimiter= ';')
  data = list(reader)
  
Y = list()
for row in data:
  if row['movieName'] == 'zodiac':
    Y.append(row['Author'])

print(Y)

#Extract movies that have been watched by Authors from list Y and put it in list Z
Z = list()
for row in data:
  if row['Author'] in Y:
    Z.append(row['movieName'])
    
print(Z)


#Makes a textfile with the results of Z
textfile = open('resultsZ.txt','w')
for element in Z:
    textfile.write(element+"\n")
textfile.close()