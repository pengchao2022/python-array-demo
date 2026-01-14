def input_array():
    numbers = input("Enter numbers separated by spaces: ").split()
    return [int(num) for num in numbers]





def main():
    arr1 = input_array()
    arr2 = input_array()
    merged_array = arr1 + arr2
    print("first array is:", arr1)
    print("second array is:", arr2)
    print("merged array is:", merged_array)



if __name__ == "__main__":
    main()

    