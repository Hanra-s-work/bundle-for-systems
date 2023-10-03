from sys import argv, exit

print("Hello World !")
if len(argv) > 1:
    for index, item in enumerate(argv[1:]):
        print(f"{index}:  '{item}'")
    exit(0)
exit(84)