def get_user_answer(dir, number):

    while True:
        if dir>0:
            result = input(f'Is the number greater than {number}? (y/n): ')
        else:
            result = input(f'Is the number less than {number}? (y/n): ')

        if result =='y':
            return True
        elif result== 'n':
            return False


def find_user_number():
    print('Think and remember the number from 1 ... 100\nand I will try to guess it ;)')
    max_number=100
    min_number=1
    dir=1

    dif_number=int( (max_number-min_number)/2+min_number)

