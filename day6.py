# method of strings 
a = "hello world"
print(len(a))  # This will print the length of the string 'a', which is 11
print(a[0:5])  # This will print the substring "hello" from index 0 to 4
print(a.upper())  # This will convert the string to uppercase, resulting in "HELLO WORLD"
print(a.lower())  # This will convert the string to lowercase, resulting in "hello world"
print(a.capitalize())  # This will capitalize the first letter of the string, resulting in "Hello world"
print(a.title())  # This will capitalize the first letter of each word in the string, resulting in "Hello World"
print(a.strip())  # This will remove any leading or trailing whitespace from the string, resulting in "hello world"
print(a.replace("world", "Python"))  # This will replace the substring "world" with "Python", resulting in "hello Python"
print(a.split())  # This will split the string into a list of words, resulting in ["hello", "world"]
print(a.find("world"))  # This will return the index of the first occurrence of the substring "world", resulting in 6
print(a.count("o"))  # This will count the number of occurrences of the character "o" in the string, resulting in 


b= "welcome to python programming"
print(b.center(50))  # This will center the string 'b' within a field of width 50, padding with spaces on both sides