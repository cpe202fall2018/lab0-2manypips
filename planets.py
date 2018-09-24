def weight_on_planets():
   weight = float(input("What do you weigh on earth? "))
   mars = 0.38 * weight
   jupiter = 2.34 * weight
   print("\nOn Mars you would weigh",mars,"pounds.\nOn Jupiter you would weigh",jupiter,"pounds.")
   
if __name__ == '__main__':
   weight_on_planets()