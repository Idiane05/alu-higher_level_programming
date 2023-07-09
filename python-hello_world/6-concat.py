#!/usr/bin/python3
def concat_strings(string1, string2):
"""Concatenates two strings and removes trailing whitespace."""
str1 = str1.lstrip()
str2 = str2.lstrip()
return str1 + " " + str2
print(concat_strings("Holberton", "School"))
