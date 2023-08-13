fruit = ["apple","pear","orange","grape"];

for i in range (0,len(fruit)):
    print(fruit[i]);

fruit.remove(input("What to remove?\n"));
fruit.append(input("What to add?\n"));

for i in range (0,len(fruit)):
    print(fruit[i]);
