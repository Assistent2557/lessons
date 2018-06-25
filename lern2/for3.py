class_scores = [{'school_class': '4a', 'scores': [3,4,2,5,3]},
                {'school_class': '4b', 'scores': [2,3,5,4,2]},
                {'school_class': '4c', 'scores': [5,2,4,5,2]}]

def sum_list(list):
    res = 0
    for i in list:
        res += i # res = res + i
    return res

# первый фор
all_class = []
for i in class_scores:
    all_class = all_class + i['scores']

print("Среднее по по школое:", sum_list(all_class) / len(all_class))

# второй фор
for element in class_scores:
    #print(element)
    my_dict = element["scores"]  # Здесь лежит словарь с ключями "school_class" and "scores"
    avg_class = sum_list(my_dict) / len(my_dict) 
    print( "Среднее по классу " + element["school_class"] + ":" , avg_class)

print("\n")
for x in range(2,10):
    print(x)

print("\n")
for x in range(15)[2:10]:
    print(x)