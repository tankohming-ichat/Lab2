
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    listholder = []

    #n = int(input("How many values are you entering?"))

    #for z in range(0, n):
    x = str(input())
    #listholder.append(x)
    list = x.split(",")

    for i in range(0, len(list)):
        list[i] = float(list[i])

    return list

def calc_average(temp_list):
    tempsum = 0
    for i in range(0, len(temp_list)):
        tempsum += temp_list[i]
    avg_temp = tempsum/len(temp_list)
    return avg_temp

def calc_min_max(temp_list):
    min=temp_list[0]
    max=temp_list[0]
    for i in range(0,len(temp_list)):
        if(min>temp_list[i]):
            min = temp_list[i]

        if (max < temp_list[i]):
            max = temp_list[i]

    listholder = [min,max]
    return listholder


def sort_temperature(temp_list):
    temp_list.sort()
    return temp_list

def calc_median_temperature(temp_list):
    mid = len(temp_list) // 2
    res = (temp_list[mid] + temp_list[~mid]) / 2 # ~ operator is bitwise inverse,so when list.len is even,
                                                 # e.g. 2,mid = 2 and ~mid = -3 so it takes the 3rd index and 2nd index
    return res;

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    avgTemp = calc_average(temp_list)
    minmax_list = calc_min_max(temp_list)
    sorted_list = sort_temperature(temp_list)
    medianTemp = calc_median_temperature(sorted_list)
    print("The median temperature of the values that you entered is: ", medianTemp)
    print("The average temperature of the values that you entered is: ",avgTemp)
    print("The lowest temperature you entered is: ",minmax_list[0],end='\n')
    print("The highest temperature you entered is: ",minmax_list[1])


if __name__ == "__main__":
    main()

