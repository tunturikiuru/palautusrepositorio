#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") #muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"Lukujen {x} ja {y} summa on {summa(x, y)}") #bugikorjaus-branch
print(f"Lukujen {x} ja {y} summa on {erotus(x, y)}") #bugikorjaus-branch

logger("lopetetaan")
print("bugikorjaus") #lisäys bugikorjaus-branchissa
