# def celsius_para_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_para_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# # Exemplo de uso
# temperatura_celsius = 25
# temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit:.2f}°F")

# # Agora, vamos converter de Fahrenheit para Celsius
# nova_temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
# print(f"{temperatura_fahrenheit:.2f}°F é igual a {nova_temperatura_celsius:.2f}°C")

# Exemplo 2

def km_para_milhas(km):
    milhas = km / 1.60934
    return milhas

def milhas_para_km(milhas):
    km = milhas * 1.60934
    return km

# Exemplo de uso
distancia_km = 100
distancia_milhas = km_para_milhas(distancia_km)

print(f"{distancia_km} km é igual a {distancia_milhas:.2f} milhas")

# Agora, vamos converter de milhas para quilômetros
nova_distancia_km = milhas_para_km(distancia_milhas)
print(f"{distancia_milhas:.2f} milhas é igual a {nova_distancia_km:.2f} km")
