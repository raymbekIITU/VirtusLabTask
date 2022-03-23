import csv
import collections

happiness_us_ca_aus = collections.defaultdict(list)
# Reading first CSV file
with open('happiness_US_Canada_Australia.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for k, v in row.items():
            happiness_us_ca_aus[k].append(v)


happiness_eu = collections.defaultdict(list)
# Reading second CSV file
with open('happiness_europe.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for k, v in row.items():
            happiness_eu[k].append(v)

join_type = input("Insert a join type:")

def join(join_type):
    match join_type:
        case ("inner"|"Inner"|"INNER"):
            print( "\nIt should be return only common values, but I have no idea how to show it.\n")
            result = []
            for value in happiness_us_ca_aus["Mean_value"]:
                if value in happiness_eu["Mean_value"]:
                    result.append(value)
                else:
                    print(False)
            # I am returning only common column values
            return result
        case ("left"|"Left"|"LEFT"):
            print("\nIt should be return all values from left table plus common values from right table.\n")
            result = []
            for value in happiness_us_ca_aus["Mean_value"]:
                if value in happiness_eu["Mean_value"]:
                    result.append(happiness_us_ca_aus | happiness_eu)
                else:
                    print(False)
            return result
        case ("right"|"Right"|"RIGHT"):
            print("\nIt should be return all values from right table plus common values from left table.\n")
            result = []
            for value in happiness_us_ca_aus["Mean_value"]:
                if value in happiness_eu["Mean_value"]:
                    result.append(happiness_us_ca_aus | happiness_eu)
                else:
                    print(False)
            return result
        case _:
            print( "\nIt should be return only common values, but I have no idea how to show it.\n")
            result = []
            for value in happiness_us_ca_aus["Mean_value"]:
                if value in happiness_eu["Mean_value"]:
                    result.append(value)
                else:
                    print(False)
            # I am returning only common column values
            return result

print(join(join_type))