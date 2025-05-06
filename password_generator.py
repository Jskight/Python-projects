import random

print("""
$$$$$$$\                                      $$$$$$\                      
$$  __$$\                                    $$  __$$\                     
$$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\       $$ /  \__| $$$$$$\  $$$$$$$\  
$$$$$$$  |\____$$\ $$  _____|$$  _____|      $$ |$$$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\        $$ |\_$$ |$$$$$$$$ |$$ |  $$ |
$$ |     $$  __$$ | \____$$\  \____$$\       $$ |  $$ |$$   ____|$$ |  $$ |
$$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |      \$$$$$$  |\$$$$$$$\ $$ |  $$ |
\__|      \_______|\_______/ \_______/        \______/  \_______|\__|  \__|
""")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*?'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Password Length: ')
len = int(length)

print('\nPasswords:')

for pwd in range(number):
    passwords = ''
    for c in range(len):
        passwords += random.choice(chars)
    print(passwords)
