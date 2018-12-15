def solver():
    array_size = int(input())
    array = [int(x) for x in input().split()]
    
    ease_array(array_size, array)
    
    
def ease_array(size, array):
    num_zeroes = 0
    for i in range(size):
        if i != (size - 1):
            if(array[i] == array[i+1]) and (array[i] != 0):
                array[i] *= 2
                array[i+1] = 0
                
        if array[i] != 0:
            print(array[i], end=' ', flush=True)

        else:
            num_zeroes += 1
        
    for i in range(num_zeroes):
        print(0, end=' ', flush=True)
        
# Follows the input format for geekforgeeks
# Num test cases
# Size of array to be eased
# array elements on one line
def main():
    tests = int(input())
    for i in range(tests):
        solver()
        # for the new line.
        print()
main()