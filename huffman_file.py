# auxiliary function for converting 0/1-string to int
def to_int(byte) :
    assert(len(byte)==8)
    res = 0
    for bit in byte :
        if bit == '1' :
            res = res * 2 + 1
        else :
            res = res * 2
    return res

'''
The given dictonary and binary encoding )in form of a 0/1-String) is written 
to the file given in filename.
This only works for pure ascii dictonaries. No special characters are allowed.
The file constist of a number indicating the size of the dictonary, the dictonary 
itself and finally the code. It is assumed that the length of the code is a 
multiple of 8, so that it exactly fits into bztes. If the 0/1-String has the 
wrong length, an exception is thrown.
'''
def write_coding(filename,dict,code) :
    if len(code) % 8 != 0 :
        raise ('Bit-String has to be of size devidable by 8. Given \
                Bit-String is of length '+str(len(code)))
    else :
        dict_str = ''
        for key in dict :
            dict_str = dict_str + key + str(dict[key]) + ','
    
        binary = bytearray([])
        i = 0
        while i < len(code) :
            byte_str = code[i:i+8]
            #print(byte_str)
            binary.append(to_int(byte_str))
            i = i + 8
    
        f = open(filename,'bw')
        length_str = str(len(dict_str))+'\n'
        f.write(bytearray(length_str.encode('ascii')))
        f.write(bytearray(dict_str.encode('ascii')))
        f.write(binary)
        f.close()
        
'''
Function to read a dictonary and a Bit-String represantation from a file created 
by write_coding. It returns the dictonary and a 0/1-String. The length of the 
0/1-String will be a multiple of 8. This function only works for pure 
ASCII-dictonaries. No special characters are allowed.
'''
def read_coding(filename) :
    f = open(filename,'br')
    binary = f.read()
    f.close()
    i = 0
    while binary[i] != 10 :
        i = i + 1
    length = int(binary[0:i].decode('ascii'))
    dict_str = binary[i+1:i+length]
    binary = binary[i+length+1:]
    print(dict_str)
    dict_str = dict_str.decode('ascii')
    dict = {}
    i = 0
    while i < len(dict_str) :
        char = dict_str[i]
        j = i + 1
        while j < len(dict_str) and dict_str[j] != ',' :
            j = j + 1
        dict[dict_str[i+1:j]] = char
        i = j + 1
    bit_str = ''
    for b in binary :
        byte = bin(b)[2:]
        byte = '0'*(8-len(byte)) + byte
        bit_str = bit_str + byte
    return dict, bit_str
