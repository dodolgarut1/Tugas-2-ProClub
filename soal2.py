klub_a = input("Klub A: ")
klub_b = input("Klub B: ")
arrMenang = []

i = 0
count = 1
while (i < 1):
    print("Pertandingan",count,": ",end="")
    skor = list(map(int, input().split()))

    if (skor[0] < 0) or (skor[1] < 0):
        i += 1
        break

    if (skor[0] < skor[1]):
        arrMenang.append(klub_b)
    elif (skor [0] == skor[1]):
        arrMenang.append("Draw")
    else:
        arrMenang.append(klub_a)
    count += 1

count = 1
for i in arrMenang:
    print("Hasil ",count,":",i)
    count += 1
print("Pertandingan selesai")




    