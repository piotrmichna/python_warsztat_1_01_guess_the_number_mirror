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

