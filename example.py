from usacapi import USACApi


u = USACApi()

# prints json of all USAC colligate clubs
print(u.getCollegiateClubs())


