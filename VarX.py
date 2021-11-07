import csv
                    
with open('userReviews.csv', encoding='utf-8-sig') as reviews:
  reader = csv.DictReader(reviews,delimiter= ';')
  data = list(reader)

# Place values in list X
X = list()
for row in data:
  X.append(row['Author'])

print(X)