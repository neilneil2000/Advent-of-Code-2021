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
    target_output = {0}

    for i in range(13,6,-1):
        digits[i].set_outputs(target_output)
        start = time.perf_counter()
        digits[i].calculate_valid_inputs()
        end = time.perf_counter()
        target_output = digits[i].valid_inputs
        print(f'{len(target_output)} Valid Inputs found in { int(end-start)} seconds ')
    pass

    for a in range(1,10):
        a_out = digits[0].attempt(a,0)
        for b in range(1,10):
            b_out = digits[1].attempt(b,a_out)
            for c in range(1,10):
                c_out = digits[2].attempt(c, b_out)
                for d in range(1,10):
                    d_out = digits[3].attempt(d, c_out)
                    for e in range(1,10):
                        e_out = digits[4].attempt(e, d_out)
                        for f in range(1,10):
                            f_out = digits[5].attempt(f, e_out)
                            if True: #if_out in digits[6].valid_inputs:
                                for g in range(1,10):
                                    g_out = digits[6].attempt(g, f_out)
                                    if True: #g_out in digits[7].valid_inputs:
                                        for h in range(1,10):
                                            h_out = digits[7].attempt(h, g_out)
                                            if h_out in digits[8].valid_inputs:
                                                for i in range(1,10):
                                                    i_out = digits[8].attempt(i, h_out)
                                                    if i_out in digits[9].valid_inputs:
                                                        for j in range(1,10):
                                                            j_out = digits[9].attempt(j, i_out)
                                                            if j_out in digits[10].valid_inputs:
                                                                for k in range(1,10):
                                                                    k_out = digits[10].attempt(k, j_out)
                                                                    if k_out in digits[11].valid_inputs:
                                                                        for l in range(1,10):
                                                                            l_out = digits[11].attempt(l, k_out)
                                                                            if l_out in digits[12].valid_inputs:
                                                                                for m in range(1,10):
                                                                                    m_out = digits[12].attempt(m, l_out)
                                                                                    if m_out in digits[13].valid_inputs:
                                                                                        for n in range(1,10):
                                                                                            n_out = digits[13].attempt(n, m_out)
                                                                                            if n_out == 0:
                                                                                                print(f'SOLUTION FOUND! {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}')
                                                                                                print(f'z_0 = 0')
                                                                                                print(f'z_1 = {a_out}')
                                                                                                print(f'z_2 = {b_out}')
                                                                                                print(f'z_3 = {c_out}')
                                                                                                print(f'z_4 = {d_out}')
                                                                                                print(f'z_5 = {e_out}')
                                                                                                print(f'z_6 = {f_out}')
                                                                                                print(f'z_7 = {g_out}')
                                                                                                print(f'z_8 = {h_out}')
                                                                                                print(f'z_9 = {i_out}')
                                                                                                print(f'z_10 = {j_out}')
                                                                                                print(f'z_11 = {k_out}')
                                                                                                print(f'z_12 = {l_out}')
                                                                                                print(f'z_13 = {m_out}')
                                                                                                print(f'z_14 = {n_out}')
                                                                                                return

    for a in range(9,0,-1):
        a_out = digits[0].attempt(a,0)
        for b in range(9,0,-1):
            b_out = digits[1].attempt(b,a_out)
            for c in range(9,0,-1):
                c_out = digits[2].attempt(c, b_out)
                for d in range(9,0,-1):
                    d_out = digits[3].attempt(d, c_out)
                    for e in range(9,0,-1):
                        e_out = digits[4].attempt(e, d_out)
                        for f in range(9,0,-1):
                            f_out = digits[5].attempt(f, e_out)
                            if True: #if_out in digits[6].valid_inputs:
                                for g in range(9,0,-1):
                                    g_out = digits[6].attempt(g, f_out)
                                    if True: #g_out in digits[7].valid_inputs:
                                        for h in range(9,0,-1):
                                            h_out = digits[7].attempt(h, g_out)
                                            if h_out in digits[8].valid_inputs:
                                                for i in range(9,0,-1):
                                                    i_out = digits[8].attempt(i, h_out)
                                                    if i_out in digits[9].valid_inputs:
                                                        for j in range(9,0,-1):
                                                            j_out = digits[9].attempt(j, i_out)
                                                            if j_out in digits[10].valid_inputs:
                                                                for k in range(9,0,-1):
                                                                    k_out = digits[10].attempt(k, j_out)
                                                                    if k_out in digits[11].valid_inputs:
                                                                        for l in range(9,0,-1):
                                                                            l_out = digits[11].attempt(l, k_out)
                                                                            if l_out in digits[12].valid_inputs:
                                                                                for m in range(9,0,-1):
                                                                                    m_out = digits[12].attempt(m, l_out)
                                                                                    if m_out in digits[13].valid_inputs:
                                                                                        for n in range(9,0,-1):
                                                                                            n_out = digits[13].attempt(n, m_out)
                                                                                            if n_out == 0:
                                                                                                print(f'SOLUTION FOUND! {a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}')
                                                                                                print(f'z_0 = 0')
                                                                                                print(f'z_1 = {a_out}')
                                                                                                print(f'z_2 = {b_out}')
                                                                                                print(f'z_3 = {c_out}')
                                                                                                print(f'z_4 = {d_out}')
                                                                                                print(f'z_5 = {e_out}')
                                                                                                print(f'z_6 = {f_out}')
                                                                                                print(f'z_7 = {g_out}')
                                                                                                print(f'z_8 = {h_out}')
                                                                                                print(f'z_9 = {i_out}')
                                                                                                print(f'z_10 = {j_out}')
                                                                                                print(f'z_11 = {k_out}')
                                                                                                print(f'z_12 = {l_out}')
                                                                                                print(f'z_13 = {m_out}')
                                                                                                print(f'z_14 = {n_out}')
                                                                                                return




  
    

if __name__ == "__main__":
    main()