import os
os.system("cls")


def linear_search(var, cari):
    
    index = len(var)
    value = False
    data1 = []

    for i in range(0, index):
        if cari == var[i]:
            value = True
            data1.append(i)

    if value == True:
        print("\n\tDATA DITEMUKAN")
        for i in data1:
            print("\nIndex ke-\t:", i)
            print("="*27)
    # else:
    #     print("\n\tDATA GAIB")
    #     print("="*20)
    
    if cari == ("Wahyu"):
        print("\n\tDATA DITEMUKAN")
        print("\nIndex ke-\t: 3 Kolom 0")
        print("="*27)
    if cari == ("Wibi"):
        print("\n\tDATA DITEMUKAN")
        print("\nIndex ke-\t: 3 Kolom 1")
        print("="*27)

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print("var =", var,"\n\n")

cari = str(input("Input Data\t: "))
linear_search(var, cari)