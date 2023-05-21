# slicing: [start:stop(excluded):step]
# default steps size = 1
# default stop index = length of string
# default start index = 0

# https://www.youtube.com/watch?v=eH6GCyHnWTA 

s = "Multimedia Programming"
s1 = s[:10] # Multimedia (only stop index, no start index)
s2 = s[22:] # Programming (only start index, no stop index)

gr = s[14:19] + s[9:10] + s[12:13] # grammar

print(s1)
