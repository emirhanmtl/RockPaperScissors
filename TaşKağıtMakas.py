import random
import time

print("Çıkmak için x'e basın.")

while True:

    ihtimaller = ["taş", "kağıt", "makas"]
    bilgisayar_secimi = random.choice(ihtimaller)
    kullanıcı_secimi = input("Taş, Kağıt, Makas ?\n")

    if (kullanıcı_secimi == bilgisayar_secimi):
        
        print(f"Herkesin seçimi {kullanıcı_secimi}. Berabere!")

    elif (kullanıcı_secimi == "taş"):

        if (bilgisayar_secimi == "makas"):

            print("Bilgisayar düşünüyor...")
            time.sleep(2)
            print("Bilgisayarın seçimi makas.")
            print("Taş Makası ezer. Sen Kazandın!")

        else:

            print("Bilgisayar düşünüyor...")
            time.sleep(2)
            print("Bilgisayarın seçimi kağıt.")
            print("Kağıt taşı kaplar. Kaybettin.")

    elif (kullanıcı_secimi == "kağıt"):

        if (bilgisayar_secimi == "taş"):

            print("Bilgisayar düşünüyor...")
            time.sleep(2)
            print("Bilgisayarın seçimi taş.")
            print("Kağıt taşı kaplar. Sen Kazandın!")

        else:

            print("Bilgisayar düşünüyor...")
            time.sleep(2)
            print("Bilgisayarın seçimi makas.")
            print("Makas kağıdı keser. Kaybettin.")

    elif (kullanıcı_secimi == "makas"):

        if (bilgisayar_secimi == "kağıt"):

            print("Bilgisayar düşünüyor...")
            time.sleep(2)
            print("Bilgisayarın seçimi kağıt.")
            print("Makas kağıdı keser. Sen Kazandın!")

        else:

            print("Bilgisayar düşünüyor...")
            time.sleep(2)
            print("Bilgisayarın seçimi taş.")
            print("Taş makası ezer. Kaybettin.")

    if (kullanıcı_secimi.lower() == "x"):

        break