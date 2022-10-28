import argparse
parser = argparse.ArgumentParser()
parser.add_argument(dest = "name")
args = parser.parse_args()
print(args)
names = ["first_name", "last_name"]
input_name = args.name.split(" ")
mydict = dict(zip(names, input_name ))

print(mydict)