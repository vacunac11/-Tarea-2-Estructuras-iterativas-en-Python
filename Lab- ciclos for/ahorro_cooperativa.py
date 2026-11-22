BONO_FIDELIDAD = 0.01  # 1 % del saldo cada 12 meses

# Datos del socio 
deposito = float(input("Depósito mensual ($): "))
meses = int(input("Plazo (meses): "))
while meses <= 0:
    print("El plazo debe ser de al menos 1 mes.")
    meses = int(input("Plazo (meses): "))
tasa_anual = float(input("Tasa de interés anual (%): "))
meta = float(input("Meta de ahorro ($): "))

tasa_mensual = tasa_anual / 100 / 12

# Tabla mes a mes 
saldo = 0.0
total_depositado = 0.0
total_intereses = 0.0
total_bonos = 0.0
meta_alcanzada = False
mes_meta = 0

print()
print(f"{'Mes':>4} {'Depósito':>10} {'Interés':>9} {'Bono':>8} {'Saldo':>11}")

for mes in range(1, meses + 1):
    saldo += deposito
    total_depositado += deposito

    interes = saldo * tasa_mensual
    saldo += interes
    total_intereses += interes

    bono = 0.0
    if mes % 12 == 0:
        bono = saldo * BONO_FIDELIDAD
        saldo += bono
        total_bonos += bono

    print(f"{mes:>4} {deposito:>10.2f} {interes:>9.2f} {bono:>8.2f} {saldo:>11.2f}")

    if not meta_alcanzada and saldo >= meta:
        meta_alcanzada = True
        mes_meta = mes

# Resumen 
print()
print(f"Total depositado: ${total_depositado:,.2f}")
print(f"Intereses ganados: ${total_intereses:,.2f}")
print(f"Bonos recibidos: ${total_bonos:,.2f}")
print(f"Saldo final: ${saldo:,.2f}")
if meta_alcanzada:
    print(f"La meta de ${meta:,.2f} se alcanza en el mes {mes_meta}.")
else:
    print(f"La meta de ${meta:,.2f} no se alcanza; faltan ${meta - saldo:,.2f}.")

# Comparar tasas
print()
print("Comparación de tasas para el mismo plan:")
for tasa in range(4, 13, 2):
    tm = tasa / 100 / 12
    s = 0.0
    for mes in range(1, meses + 1):
        s += deposito
        s += s * tm
        if mes % 12 == 0:
            s += s * BONO_FIDELIDAD
    print(f" {tasa:>2} % anual -> saldo final ${s:,.2f}")