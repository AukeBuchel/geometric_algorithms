
bfLines = []
psLines = []

with open("outpurs/bf.txt", "r") as f:
    bfLines = f.readlines()
with open("outpurs/ps.txt", "r") as f:
    psLines = f.readlines()
    
# remove empty lines
for line in bfLines:
    if len(line.strip()) == 0:
        bfLines.remove(line)
for line in psLines:
    if len(line.strip()) == 0:
        psLines.remove(line)
    
# compare, which lines are different
# remove all lines bfLines that are also in psLines
if len(bfLines) > len(psLines):
    print("bf detected more")
    for line in psLines:
        if line in bfLines:
            bfLines.remove(line)
    if len(bfLines) > 0:
        print("============== Brute force ==============")
        for line in bfLines:
            print("+ " + line)
elif len(psLines) > len(bfLines):
    print("ps detected more")
    for line in bfLines:
        if line in psLines:
            psLines.remove(line)
    if len(psLines) > 0:
        print("============== Plane sweep ==============")
        for line in psLines:
            print("+ " + line)
    

print("Differences:")
