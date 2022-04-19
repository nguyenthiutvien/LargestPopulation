
country1=input("country 1:")
country2=input("country 2:")
country3=input("country 3:")
def largestCountry(country1,country2,country3):
    population=[1439323776,1380004385,331002651,273523615,220892340]
    countries=["China","India","USA","Indonesia","Pakistan"]
    b=0
    for i in range(5):
        if country1==countries[i]:
            country1=int(population[i])
            b=b+1
        if country2==countries[i]:
            country2=int(population[i])
            b=b+1
        if country3==countries[i]:
            country3=int(population[i])
            b=b+1
    if b==3:
        largest=max(country1,country2,country3)
        for i in range(5):
            if largest==population[i]:
                largest=countries[i]
        return "The largest country is:" + largest
    else:
        return "Error, bad country name entered"
print(largestCountry(country1,country2,country3))

    

        

    
 
 
