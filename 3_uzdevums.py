# Uzraksti programmu, kurā  dators izvēlas 100 
# skaitļus robežās no 101 līdz 500. Izvēlētie 
# skaitļi tiek izvadīti terminālī.

import random

#cik skaitļi jāizvēlas
skaitļi=100
#kādas ir robešas
min_rob=101
max_rob=501

#jāveido cikls, jo jāģenerē 100 skaitļi
for i in range(100):
    random_skaitlis=random.randint(101, 501)
print(random_skaitlis)

