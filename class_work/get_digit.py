# number = 50
# position = 0.01
def get_digit(number, position) :
    """return digit at position in number, counting from right"""
    return number//(10 ** position)%10
