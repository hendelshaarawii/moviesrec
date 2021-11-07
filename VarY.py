import csv
                    
with open('userReviews.csv', encoding='utf-8-sig') as reviews:
  reader = csv.DictReader(reviews,delimiter= ';')
  data = list(reader)

# Extract Authors that reviewed on favorite movie from X list into Y list
Y = list()
for row in data:
  if row['movieName'] == 'zodiac':
    Y.append(row['Author'])

print(Y)