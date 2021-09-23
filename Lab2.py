conversionFactor=31536000
births=float(input("input births per second"))
deaths=float(input("input deaths per second"))
migrations=float(input("input migrations per second"))
years=float(input("please input how many years into the future you wish to calculate"))
initialPop=float(input("please input the initial population"))

totalBirths=births*conversionFactor*years
totalDeaths=deaths*conversionFactor*years
totalMigrations=migrations*conversionFactor*years

prediction=initialPop+totalBirths-totalDeaths+totalMigrations
# print(totalBirths)
# print(totalDeaths)
print(prediction)

