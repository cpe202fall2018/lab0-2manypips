def weight_on_planets():
   weight = float(input("Enter your weight here: "))
   mars = 0.38 * weight
   jupiter = 2.34 * weight
   print("\n","On Mars you would weigh ", mars, " pounds.", "\n", "On Jupiter you would weigh ", jupiter, " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()