print(len('xxx'))
#add meg a szó 3-6. betűjét! 0-val kezdünk, 7. betű (6. index) már nincs benne!
print("Agyagosszergény"[3:6])
print("Agyagosszergény"[0:3])
#nem adom meg honnan kezdje -->elejéről kezdi, ha a végét nem adom meg, akkor a string végéig megy
print("Agyagosszergény"[:6])
#hányadiktól hányadikig hányasával (lépésköz)
print("Agyagosszergény"[3:10:2])

#visszafelé a szó! (elejétől a végéig mínusz egyesével)
print("Agyagosszergény"[::-1])

print("Agyagosszergény".replace("A", "E"))
print("Agyagosszergény".upper())


print("Agy" in "Agyagosszergény")
print("agy" in "Agyagosszergény")


name="Komlóska"
print(name.lower())
print(name)

#srting feldarabolása - darabolást követően több értéket tartalmaz a string (tömb!)
line = "Windowa 2000;Windows Server 2000"
parts = line.split(";")
print(parts[0])
print(parts[1])
