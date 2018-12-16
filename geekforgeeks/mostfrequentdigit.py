def frequentdigit():
    number = input()
    digits = {}
    
    for digit in number:
        if digits.get(digit) != None:
            digits[digit] += 1
        else:
            digits[digit] = 1
    
    max_key = number[0]
    for k,v in digits.items():
        if digits[max_key] < v:
            max_key = k
        elif digits[max_key] == v:
            if max_key < k:
                max_key = k
    
    print(int(max_key))
        
    

def main():
    tests = int(input())
    for i in range(tests):
        frequentdigit()

