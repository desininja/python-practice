# square = lambda x:x*x
# sum = lambda x,y:x+y 
# print(square(3))
# print(sum(3,62))



students = [('Alice', 88), ('Bob', 92), ('Charlie', 78)]

# Sort by the score (the item at index 1)

print(f"Before sorting:, {students}")
students = sorted(students,key=lambda x:x[1])
print(f"After sorting:, {students}")