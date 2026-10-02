person1={
  "name":"asif khan",
  "age":3,
  "gender":"male",
  "monthly income":43
 
}
person2={
"name":"khan mia",
  "age":27,
  "gender":"male",
  "monthly income":43

} 
for value in person1.values():
    print(value)

print('\n')

for key in person1.keys():
    print(key)

for key,value in person2.items():
  print(f'{key}:{value}')
 