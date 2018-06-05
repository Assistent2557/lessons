print("Введите возраст")
age = int(input())

if age == 0:
   print("Вы не роделись")
elif 1 < age <= 7:
   print("Ходите в сад или ясли")
elif 7 < age <= 17:
   print("Учитесь в школе")
elif 17 < age <= 23:
   print("Учитесь в ВУЗЕ")
elif 23 < age <= 65:
   print("Работаете")
elif 65 < age <= 100:
   print("Вы пенсионер")
else:
   print(age)