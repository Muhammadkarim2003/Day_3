yil = int(input("Yilni kiriting: "))

if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print(f"{yil}-yil kabisa yili")
        else:
            print(f"{yil}-yil kabisa yili emas")
    else:
        print(f"{yil}-yil kabisa yili")
else:
    print(f"{yil}-yil kabisa yili emas")