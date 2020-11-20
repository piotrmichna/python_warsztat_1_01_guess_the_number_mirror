def get_user_answer(number):
    """the function gets the player's answers
    and checks for errors
    :parameter: integer

    :return: boolean
    """
    while True:
        result = input(f'Is the number greater than {number}? (y/n): ')
        result = result.lower()

        if result == 'y':
            return True
        elif result == 'n':
            return False


def find_user_number():
    """Main function Guess The Number-mirror
    function try to find the user number"""

    print('Think and remember the number from 1 ... 100\nand I will try to guess it ;)')
    max_number = 100
    min_number = 1

    while max_number - min_number > 0:
        secret_number = int((max_number - min_number) / 2 + min_number)

        if get_user_answer(secret_number):
            min_number = secret_number + 1
        else:
            max_number = secret_number

    secret_number = int((max_number - min_number) / 2 + min_number)
    print(f'The top secret number is {secret_number}')


if __name__ == '__main__':
    find_user_number()
