import sys, pygame

def display_message(message, number_of_times):
    i = 0
    while(i < number_of_times):
        sys.stdout.write(message + " | " + str((i + 1)) + "\n")
        i += 1
def get_message():
    sys.stdout.write("What would you like to display?: ")
    message = sys.stdin.readline().strip()
    return message

def get_message_amount():
    sys.stdout.write("Enter the amount of times you want your message to display: ")
    amount = int(sys.stdin.readline())
    return amount

def message_manager():
    message = get_message()
    amount = get_message_amount()
    display_message(message, amount)

def get_darkest_secret():
    sys.stdout.write("What's your most shameful secret?\n")
    secret = sys.stdin.readline()
    return secret

def display_secret(secret):
    sys.stdout.write("We've sent your secret to your mum, your dad, your grandad, your grandma, your aunty, your uncle, your brother, your sister, and your dog\n") #Diabolical, even the dog?! | Always include the dog
    sys.stdout.write("Now everyone knows that you " + secret)

def darkest_secret_manager():
    secret = get_darkest_secret
    display_secret(secret)

    #I don't think secret is spelled right, looks off. Could just be me
    #I think it's fine. I do that sometimes too.
darkest_secret_manager()
message_manager()
#Stop writing until we get James in here
#✔