
def HEX_char_To_Int(c_in_char):

    #[Input] value should be String <'0'~'9'>  or  <'A'~'F'> or <'a' ~ 'f'>
    #[Output] value should be  Int <0 ~ 15> 
    
    # HEX char to Int   EX: '5'->Int(5)   'a'->Int(10)   'C'->Int(12)
    try:
        c_in = ord(c_in_char)   # char To Int  Ex: '1' -> Int(49)   'A' -> Int(65)

        if(c_in >= 0x30 and c_in <= 0x39):     # '0' ~ '9'  => Int(0~9)
            return c_in - 0x30
        elif (c_in >= 0x41 and c_in <= 0x46):  # 'A' ~ 'F'  => Int(10~15)
            return c_in - 55
        elif (c_in >= 0x61 and c_in <= 0x66):  # 'a' ~ 'f'  => Int(10~15)
            return c_in - 87
        else:
            print('input value out of range !!')
            return 0
    except:
        print('err ord() !!')
        return 0
    

def HEX_String_to_bytes(str_in):
    # [input] should be  [string]  '00 8F A5 BF'   or  '008fa5bf' 
    # [output] would be  [bytes]  b'\x00\x8f\xa5\xbf'
    out_bytes = b''
    n = 0
    byte_tmp = 0x00
    for c_in_str in str_in:

        if((ord(c_in_str) != 0x20) and (ord(c_in_str) != 0x0a)):  #skip "<space>" and "\n" 

            if(n%2==0):
                #print(16*HEX_char_To_Int(c_in_str))
                byte_tmp += 16*HEX_char_To_Int(c_in_str)
            if(n%2==1):
                #print(1*HEX_char_To_Int(c_in_str))
                byte_tmp += 1*HEX_char_To_Int(c_in_str)
                out_bytes += bytes([byte_tmp])
                byte_tmp = 0
            n+=1

    return out_bytes



if __name__ == "__main__":
    HEX_String = '00 8F A5 BF'
    bytes_output = HEX_String_to_bytes(HEX_String)
    print( "string:" , HEX_String ," -> bytes: " , bytes_output)

