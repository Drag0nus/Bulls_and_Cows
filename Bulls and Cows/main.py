

import number_generator


generated_secret_number = number_generator.generate_secret_number(4)
print("Hint - %s" % generated_secret_number)


def compare_numbers(answer):
    attempt = 0
    cow = 0
    bull = 0
    while cow != 4:
        cow = 0
        bull = 0
        guess = input("Enter number (or type 'exit' for end this): ")
        if guess == 'exit':
            break
        else:
            attempt += 1
            for i in range(0, len(guess)):
                if guess[i] in answer and guess[i] != answer[i]:
                    bull += 1
                if guess[i] == answer[i]:
                    cow += 1
            print("Attempt - %s." % attempt)
            print("Cows - %s." % cow)
            print("Bulls - %s." % bull)
    else:
        print("Victory!")
        return [cow, bull]


print(compare_numbers(generated_secret_number))
