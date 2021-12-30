from ALU_modules import ModelDigit
import time

def main():
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

    next_inputs = {0}

    for digit in digits:
        digit.set_inputs(next_inputs)
        start = time.perf_counter()
        digit.method_one()
        digit.method_two()
        end = time.perf_counter()
        next_inputs = digit.valid_outputs
        print(f'{len(digit.valid_outputs)} Valid outputs found in {int(end-start)} seconds')

    if 0 in digits[-1].valid_outputs:
        print(f'Zero Found in final output :-)')
    else:
        print(f'No zero found :-(')

    
    

if __name__ == "__main__":
    main()