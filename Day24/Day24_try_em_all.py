from ALU_modules import ModelDigit
import time

def main():
    no_digits = 14
    model_number = [9 for x in range(no_digits)]
    digits = []
    digits.append(ModelDigit(False, 12, 7))
    digits.append(ModelDigit(False, 12, 8))
    digits.append(ModelDigit(False, 13, 2))
    digits.append(ModelDigit(False, 12, 11))
    digits.append(ModelDigit(True, -3, 6))
    digits.append(ModelDigit(False, 10, 12))
    digits.append(ModelDigit(False, 14, 14))
    digits.append(ModelDigit(True, -16, 13))
    digits.append(ModelDigit(False, 12, 15))
    digits.append(ModelDigit(True, -8, 10))
    digits.append(ModelDigit(True, -12, 6))
    digits.append(ModelDigit(True, -7, 10))
    digits.append(ModelDigit(True, -6, 8))
    digits.append(ModelDigit(True, -11, 5))
    input = 0

    inputs = {i for i in range(0,26)}
    inputs = inputs.union({319,320,321,322,323,324,325,326,327,345,346,347,348,349,350,351,352,353,371,372,373,374,375,376,377,378,379,397,398,399,400,401, \
        402,403,404,405,423,424,425,426,427,428,429,430,431,449,450,451,452,453,454,455,456,457,475,476,477,478,479,480,481,482,483,501,502,503, \
            504,505,506,507,508,509,527,528,529,530,531,532,533,534,535})
    print(f'{len(inputs)} inputs to try')

    target_output = {0}
    for i in range(13,10,-1):
        digits[i].set_outputs(target_output)
        start = time.perf_counter()
        digits[i].calculate_valid_inputs()
        end = time.perf_counter()
        target_output = digits[i].valid_inputs
        print(f'{len(target_output)} Valid Inputs found in { int(end-start)} seconds ')
    pass

    for input in inputs:
        valid = False
        for i in range(9,0,-1):
            result = digits[12].attempt(i, input)
            if result in {12,13,14,15,16,17,18,19,20}:
                valid = True
        if valid == False:
            print(f'{input} not a valid input')
    
    pass


    for i,digit in enumerate(digits):
        input = digit.attempt(model_number[i], input)






if __name__ == "__main__":
    main()