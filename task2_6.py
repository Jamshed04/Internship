distance = int(input("Сколько километров хотите проехать на автомобиле? "))
liters_100 = int(input("Сколько литров топлива на 100 км? "))
tankliters = int(input("Сколько литров топлива в вашем баке? "))
if (liters_100 / 100) * distance <= tankliters:
    print("Вы сможете проехать желаемое расстояние")
else:
    print("Вы не доедете")
