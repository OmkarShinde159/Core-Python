# python Round function
# returns the nearest rounding value

print(-7//2)
print(-7/2)

print(round(3.4))
print(round(-3.6))

# convert all the values in list into round values
l = [-12.6, -56.67, 89.8, -34.3, 54.4]
map1 =map(round,l)
print(list(map1))

# convert all valuesin list into abs values
abs_map = map(abs, l)
print(set(abs_map))


