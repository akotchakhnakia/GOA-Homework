name = "ako"

new_string = ""

for i in name:
   new_string = i + new_string
print(new_string)

#index py
name ="ako"
new_name =""
for i in range(len(name)-1, -1, -1):
   new_name = new_name + name[i]
print(new_name)