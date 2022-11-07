# the AnimalBites dataset, stored in the file Health_AnimalBites.csv,
# includes information on over 9,003 animal bites which occurred near
# Louisville, Kentucky from 1985 to 2017 and includes information on
# whether the animal was quarantined after the bite occurred and
# whether that animal was rabid

# each line of the files contains several information about an animal bite:
#     • bite_date: The date the bite occurred
#     • SpeciesIDDesc: The species of animal that did the biting
#     • BreedIDDesc: Breed (if known)
#     • GenderIDDesc: Gender (of the animal)
#     • color: color of the animal
#     • vaccination_yrs: how many years had passed since the last vaccination
#     • vaccination_date: the date of the last vaccination
#     • victim_zip: the zipcode of the victim
#     • AdvIssuedYNDesc: whether advice was issued
#     • WhereBittenIDDesc: Where on the body the victim was bitten
#     • quarantine_date: whether the animal was quarantined
#     • DispositionIDDesc: whether the animal was released from quarantine
#     • headsentdate: the date the animal’s head was sent to the lab
#     • release_date: the date the animal was released
#     • ResultsIDDesc: results from lab tests (for rabies)

# the single information are separated by commas, so for example the line:
# 1985-05-05 00:00:00,DOG,,FEMALE,LIG. BROWN,1,1985-06-20 00:00:00,40229,NO,BODY,1985-05-05 00:00:00,UNKNOWN,,,UNKNOWN
# corresponds to the following bite event:
#     • bite_date: 1985-05-05 00:00:00
#     • SpeciesIDDesc:  DOG
#     • BreedIDDesc: 
#     • GenderIDDesc:  FEMALE
#     • color:  LIG. BROWN
#     • vaccination_yrs: 1
#     • vaccination_date:  1985-06-20 00:00:00
#     • victim_zip:  40229
#     • AdvIssuedYNDesc: NO
#     • WhereBittenIDDesc: BODY
#     • quarantine_date:  1985-05-05 00:00:00
#     • DispositionIDDesc:  UNKNOWN
#     • headsentdate: 
#     • release_date: 
#     • ResultsIDDesc:  UNKNOWN

# write a function to reads the file and prints the following information:
# 1. the total number of bite events (9003)
# 2. the list of breeds ('DOG', 'CAT', 'BAT', ...)
# 3. the number of events per year (1985: 1, 2009: 14, ...)

# *********** YOU CANNOT IMPORT ANY EXTRA PACKAGE ************
# *************** YOU CANNOT USE DICTIONARIES ****************

def AnimalBites(dbFile):
    with open('Health_AnimalBites.csv','r',encoding = 'utf8') as jeff:
        jeff.readline().strip().split(',')[1]
        biteList = [steve.strip().split(',') for steve in jeff]
        animalList = [steve.strip().split(',') for steve in jeff]
    
    print('Number of bite events is', len(biteList))
    print(biteList[0][1])
    animals = set(biteList[0:3][1])
    print(animals)

if __name__ == "__main__":
  AnimalBites("Health_AnimalBites.csv")