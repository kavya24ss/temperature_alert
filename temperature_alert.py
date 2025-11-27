import sys

if len(sys.argv) == 2:
    try:
        temp = int(sys.argv[1])
    except ValueError:
        print(f"Invalid temperature value: {sys.argv[1]}")
        sys.exit(1)
else:
    temp = 25

if temp > 40:
    print("hot")
elif temp > 20:
    print("Normal")
else:
    print("cold")
