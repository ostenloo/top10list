import random 

players = ["Michael Jordan","Lebron James", "Kareem Abdul Jabbar", 
           "Magic Johnson", "Wilt Chamberlain", "Bill Russell", "Larry Bird", 
           "Tim Duncan", "Shaquille O' Neal", "Kobe Bryant", "Hakeem Olajuwon", 
           "Julius Erving", "Oscar Robertson", "Moses Malone", "Jerry West", 
           "Stephen Curry", "Kevin Durant", "David Robinson", "Kevin Garnett",
           "Dirk Nowitzki", "Karl Malone", "Elgin Baylor", "George Mikan", "Charles Barkley",
           "Giannis Antetokounmpo", "Isiah Thomas", "Chris Paul", "Kawhi Leonard", "John Havlicek", 
           "John Stockton"]
           

top10list = set()

while len(top10list) < 10: 
    top10list.add(random.choice(players))
    
for x in top10list: 
    print(x)
    
