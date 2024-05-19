print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")

    float_list = [float(num) for num in str_list]
    return float_list

def calc_average_temperature(temperature_values_list):
    total = sum(temperature_values_list)
    average = total / len(temperature_values_list)
    return average

def calc_min_max_temperature(temperature_values_list):
    min_temp = min(temperature_values_list)
    max_temp = max(temperature_values_list)
    return [min_temp, max_temp]

def calc_median_temperature(temperature_values_list):
    sorted_list = sorted(temperature_values_list)
    
    n = len(sorted_list)
    if n % 2 == 0:
        # If even number of elements, median is the average of the two middle numbers
        median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        # If odd number of elements, median is the middle number
        median = sorted_list[n//2]
    
    return median

if __name__ == "__main__":
    display_main_menu()
    temperatures = get_user_input()
    print("List of temperatures: ", temperatures)

    average_temp = calc_average_temperature(temperatures)
    print("Average Temperature:", average_temp)

    min_max_temp = calc_min_max_temperature(temperatures)
    print("Min and Max Temperature:", min_max_temp)

    median_temp = calc_median_temperature(temperatures)
    print("Median Temperature:", median_temp)


