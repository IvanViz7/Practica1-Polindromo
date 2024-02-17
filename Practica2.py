inversión = int(input("Introduce el monto de tu inversión: "))
interés = float(input("introduce el interés que deseas calcular: ")) / 100
años = int(input("introduce la cantidad de años con la que deseas calcular el interes compuesto: "))

def interes_compuesto():
    int_comp = inversión
    for _ in range(años):
        int_comp *= (interés + 1)
    return int_comp



resultado = interes_compuesto()
resultado = round(resultado,2)
print(f'Tu dinero al cabo de {años} años con un interés de {interés * 100}% y con una inversión inicial de ${inversión} te dará: ${resultado}')


