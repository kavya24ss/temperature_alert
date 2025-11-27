import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = sys.argv[1]
else:
    temp = 25
if temp > 40:
    print("hot")
elif temp > 20:
    print("normal")
else:
    print("cold")
