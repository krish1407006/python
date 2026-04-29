#file IO

f = open("krish.txt", "r")
print(f.read())
f.close()

f = open("krish.txt", "r")

line = f.readline()

marks = line.split(",")

m1 = int(marks[0])
m2 = int(marks[1])
m3 = int(marks[2])

print(m1, m2, m3)


f = open("krish.txt", "w")
 
lines = ["krish\n", "krish\n", "krish\n"]

f.writelines(lines)
f.close()

