fruits = ["Watermelon", "Melon", "Apple", "Pomegranate"]
print("Accessing elements using indexing:")

print(f"First fruit is: {fruits[0]}")
print(f"Second fruit is: {fruits[1]}")
print(f"Last fruit is: {fruits[-1]}")


fruits[2] = "Banana"
print(f"Modified new list is: {fruits}")


fruits.append("watermelon")
print(f"Modified new list is: {fruits}")


fruits.remove("watermelon")
print(f"Modified new list is: {fruits}")


length = len(fruits)
print(length)


fruits.sort()
print(f"Sorted Fruits' list is: {fruits}")