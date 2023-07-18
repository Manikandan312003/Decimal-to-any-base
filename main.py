def convertToBase(number,base):
    converted=""
    while number>0:
        converted=str(number%base)+converted
        number//=base
    return converted
print(convertToBase(4,3))