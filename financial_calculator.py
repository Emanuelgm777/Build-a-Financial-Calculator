import numpy as np
import math
import sympy as sp

# Calcular la anualidad con crecimiento mensual o continuo
def annuity_calculator(principal, rate, periods, growth_type='monthly'):
    """
    Calcula la anualidad con crecimiento mensual o continuo.
    principal: monto inicial
    rate: tasa de interés anual
    periods: número de períodos (meses o años)
    growth_type: 'monthly' para crecimiento mensual, 'continuous' para crecimiento continuo
    """
    rate_monthly = rate / 12 if growth_type == 'monthly' else rate
    if growth_type == 'monthly':
        # Fórmula de anualidad con crecimiento mensual
        annuity = principal * ((rate_monthly * (1 + rate_monthly)**periods) / ((1 + rate_monthly)**periods - 1))
    elif growth_type == 'continuous':
        # Fórmula de anualidad con crecimiento continuo (crecimiento exponencial)
        annuity = principal * rate * periods
    return annuity

# Calcular el pago mensual de una hipoteca
def mortgage_payment(principal, annual_rate, months):
    """
    Calcula el pago mensual de una hipoteca.
    principal: monto del préstamo
    annual_rate: tasa de interés anual
    months: número de meses para el préstamo
    """
    monthly_rate = annual_rate / 12
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return payment

# Estimar el saldo de la inversión para la jubilación
def retirement_balance(principal, annual_rate, years):
    """
    Estima el saldo de una inversión para la jubilación.
    principal: monto inicial
    annual_rate: tasa de interés anual
    years: número de años
    """
    balance = principal * (1 + annual_rate)**years
    return balance

# Determinar cuánto tiempo hasta que una cantidad se duplique, dado la tasa
def time_to_double(rate):
    """
    Determina el tiempo necesario para que una cantidad se duplique dado la tasa de interés anual.
    rate: tasa de interés anual
    """
    time = np.log(2) / np.log(1 + rate)
    return time

# Resolver ecuaciones logarítmicas
def solve_logarithmic_equation(base, result):
    """
    Resuelve una ecuación logarítmica del tipo base^x = result.
    base: la base del logaritmo
    result: el resultado de la ecuación
    """
    x = sp.symbols('x')
    equation = sp.Eq(base**x, result)
    solution = sp.solve(equation, x)
    return solution

# Convertir a notación científica
def to_scientific_notation(number):
    """
    Convierte un número a notación científica.
    number: el número a convertir
    """
    return "{:.2e}".format(number)

# Convertir desde notación científica
def from_scientific_notation(sci_str):
    """
    Convierte una cadena de texto en notación científica de vuelta a un número.
    sci_str: la cadena en notación científica
    """
    return float(sci_str)

# Función principal para interactuar con el usuario
def main():
    print("¡Bienvenido a la Calculadora Financiera!")
    
    # Selección de opción
    print("1. Calcular Anualidad")
    print("2. Calcular Pago de Hipoteca")
    print("3. Estimar Saldo de Inversión para la Jubilación")
    print("4. Determinar Cuánto Tiempo Tomará para Duplicarse")
    print("5. Resolver Ecuación Logarítmica")
    print("6. Convertir a Notación Científica")
    print("7. Convertir de Notación Científica")
    
    choice = int(input("Selecciona una opción (1-7): "))
    
    if choice == 1:
        principal = float(input("Ingrese el monto principal: "))
        rate = float(input("Ingrese la tasa de interés anual: ")) / 100
        periods = int(input("Ingrese el número de períodos: "))
        growth_type = input("Seleccione el tipo de crecimiento (monthly/continuous): ").lower()
        result = annuity_calculator(principal, rate, periods, growth_type)
        print(f"El valor de la anualidad es: {result:.2f}")
    
    elif choice == 2:
        principal = float(input("Ingrese el monto de la hipoteca: "))
        annual_rate = float(input("Ingrese la tasa de interés anual: ")) / 100
        months = int(input("Ingrese el número de meses: "))
        result = mortgage_payment(principal, annual_rate, months)
        print(f"El pago mensual de la hipoteca es: {result:.2f}")
    
    elif choice == 3:
        principal = float(input("Ingrese el monto inicial de la inversión: "))
        annual_rate = float(input("Ingrese la tasa de interés anual: ")) / 100
        years = int(input("Ingrese el número de años: "))
        result = retirement_balance(principal, annual_rate, years)
        print(f"El saldo de la inversión después de {years} años es: {result:.2f}")
    
    elif choice == 4:
        rate = float(input("Ingrese la tasa de interés anual: ")) / 100
        time = time_to_double(rate)
        print(f"El tiempo necesario para duplicar la inversión es: {time:.2f} años")
    
    elif choice == 5:
        base = float(input("Ingrese la base del logaritmo: "))
        result = float(input("Ingrese el resultado: "))
        solution = solve_logarithmic_equation(base, result)
        print(f"La solución de la ecuación logarítmica es: {solution}")
    
    elif choice == 6:
        number = float(input("Ingrese el número a convertir: "))
        sci_str = to_scientific_notation(number)
        print(f"El número en notación científica es: {sci_str}")
    
    elif choice == 7:
        sci_str = input("Ingrese el número en notación científica: ")
        number = from_scientific_notation(sci_str)
        print(f"El número es: {number}")
    
    else:
        print("Opción no válida.")

# Ejecutar la función principal
main()
