n = int(input('Введите возраст: '))
last_dig = n % 10 # остаток от деления на 10
if 10 <n< 20: 
    print("ему ",n," лет") 
elif 1<last_dig<5: 
    print("ему",n,"года") 
elif last_dig == 1: 
    print("ему",n,"год") 
else: 
    print("ему", n, "лет")