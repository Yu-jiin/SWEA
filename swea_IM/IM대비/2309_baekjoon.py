N = 9
peoples = []
for _ in range(N):
    peoples.append(int(input()))

people_sum = 0
for people in peoples:
    people_sum += people

remain_people = people_sum - 100
# remain = 40

for i in range(N):
    for j in range(1, N):
        if peoples[i] != peoples[j] and peoples[i] + peoples[j] == remain_people:
            one = peoples[i]
            two = peoples[j]
            break

peoples.remove(one)
peoples.remove(two)
peoples.sort()

for p in peoples:
    print(p)