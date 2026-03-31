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

str= "python programming is fun"
print(str.endswith("is fun"))

print(a.count("o"))  # This will count the number of occurrences of the character "o" in the string 'a', resulting in 2

str1=" python programming is fun"
print(str1.find("is"))\

str2="python123"
print(str2.isalnum())

print(str2.isalpha()) # This will check if all characters in the string 'str2' are alphabetic, resulting in False because 'str2' contains digits as well.

str3="  "
print(str3.isspace()) # This will check if all characters in the string 'str3' are whitespace, resulting in False because 'str3' contains non-whitespace characters.

print(str2.isprintable()) # This will check if all characters in the string 'str3' are lowercase, resulting in False because 'str3' contains whitespace characters.

print(str2.istitle()) # This will check if the string 'str2' is in title case, resulting in False because 'str2' is not in title case.

c="my birthday is on 12th of june"

print(c.title()) # This will convert the string 'c' to title case, resulting in "My Birthday Is On 12Th Of June"