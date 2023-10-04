def check(code, form=(7,4)): 
    '''
    in: Hamming code as str
    out: Index for correction
    If no error is detected, the function returns -1
    '''
    if form == (7,4):
        r1, r2, i1, r3, i2, i3, i4 = map(int, list(code))
        # syndromes
        s1 = r1 ^ i1 ^ i2 ^ i4 
        s2 = r2 ^ i1 ^ i3 ^ i4
        s3 = r3 ^ i2 ^ i3 ^ i4
        if (s1 + s2 + s3) == 0: # if no error return -1
            return -1
        else:
            return int(f'{s3}{s2}{s1}', 2) - 1 #decode syndromes 
    elif form == (15, 11): 
        r1, r2, i1, r3, i2, i3, i4, r4, i5, i6, i7, i8, i9, i10, i11 = map(int, list(code))
        s1 = r1 ^ i1 ^ i2 ^ i4 ^ i5 ^ i7 ^ i9 ^ i11
        s2 = r2 ^ i1 ^ i3 ^ i4 ^ i6 ^ i7 ^ i10 ^ i11
        s3 = r3 ^ i2 ^ i3 ^ i4 ^ i8 ^ i9 ^ i10 ^ i11
        s4 = r4 ^ i5 ^ i6 ^ i7 ^ i8 ^ i9 ^ i10 ^ i11
        if (s1 + s2 + s3 + s4) == 0: # if no error return -1
            return -1
        else:
            return int(f'{s4}{s3}{s2}{s1}', 2) - 1 #decode syndromes 
    else: 
        raise ValueError('Format of code is not supported.')

def generate(code, form=(7,4), code_check=False): 
    '''
    in: Bit's as str
    out: Hamming code as str
    '''
    if form == (7,4):
        if code_check:
            res = generate(code, form) 
            if check(res, form) == -1:
                return res
            return -1
        i1, i2, i3, i4 = map(int, list(code))
        r1 = i1 ^ i2 ^ i4
        r2 = i1 ^ i3 ^ i4
        r3 = i2 ^ i3 ^ i4
        return f'{r1}{r2}{i1}{r3}{i2}{i3}{i4}'
    if form == (15,11):
        if code_check:
            res = generate(code, form) 
            if check(res, form) == -1:
                return res
            return -1
        i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11 = map(int, list(code))
        r1 = i1 ^ i2 ^ i4 ^ i5 ^ i7 ^ i9 ^ i11
        r2 = i1 ^ i3 ^ i4 ^ i6 ^ i7 ^ i10 ^ i11
        r3 = i2 ^ i3 ^ i4 ^ i8 ^ i9 ^ i10 ^ i11
        r4 = i5 ^ i6 ^ i7 ^ i8 ^ i9 ^ i10 ^ i11
        return f'{r1}{r2}{i1}{r3}{i2}{i3}{i4}{r4}{i5}{i6}{i7}{i8}{i9}{i10}{i11}'  
    else:
        raise ValueError('Format of code is not supported.')

def correct(code, form=(7,4), code_check=False):
    '''
    in: Uncorrect Hamming code as str
    out: Corrected Hamming code as str
    '''
    indx = check(code, form)
    if indx == -1: return code
    st = code[:indx] + str(1 - int(code[indx])) + code[indx + 1:]
    if code_check:
        if check(st, form) == -1:
            return st
        else:
            return -1
    return st

if __name__ == '__main__':
    code = input()
    res = check(code)
    if res == -1:
        print(f'В коде {code} нет ошибок')
    else:
        print(f'В коде {code} имеется ошибка в символе под номером {res + 1}. Корректный код: {correct(code)}')