#Tarea semana 14 Beltrán

# Definimos la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Función para mostrar el resultado
def mostrar_resultados(monto_total, porcentaje_descuento=10):
    descuento = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final = monto_total - descuento
    print(f"Monto total: ${monto_total:.2f}")
    print(f"Porcentaje de descuento: {porcentaje_descuento}%")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Monto final a pagar: ${monto_final:.2f}\n")

# Llamadas a la función
print("Primera llamada (usando descuento por defecto del 10%):")
mostrar_resultados(1000)  # Solo el monto total

print("Segunda llamada (usando un descuento del 20%):")
mostrar_resultados(1000, 20)  # Monto total y porcentaje de descuento
