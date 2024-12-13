
bfLines = []
psLines = []

with open("outpurs/bf.txt", "r") as f:
    bfLines = f.readlines()
    
with open("outpurs/ps.txt", "r") as f:
    psLines = f.readlines()
    
    
# compare, which lines are different
# remove all lines bfLines that are also in psLines
for line in psLines:
    if line in bfLines:
        bfLines.remove(line)
    
print("Plane sweep did not find the following:")    
for line in bfLines:
    print(line)