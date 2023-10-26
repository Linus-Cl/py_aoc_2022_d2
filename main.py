file_name = 'data.txt'
data = open(file_name)
total_points = 0
lines = data.readlines()

def calc_points(opponent_val, own_val):
    points = 0
    match opponent_val:
        case 'A':
            match own_val:
                case 'X':
                    points = 3
                case 'Y':
                    points = 4
                case 'Z':
                    points = 8
        case 'B':
            match own_val:
                case 'X':
                    points = 1
                case 'Y':
                    points = 5
                case 'Z':
                    points = 9
        case 'C':
            match own_val:
                case 'X':
                    points = 2
                case 'Y':
                    points = 6
                case 'Z':
                    points = 7

    return points


for line in lines:
    vals = line.split()
    total_points += calc_points(vals[0], vals[1])
     
print("The amount of total points is " + str(total_points))
