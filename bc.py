
guess = -1
while True:
    guess = int(input("Enter a number between 0 and 9:"))
    
    if guess > 9:
        continue    
    print("after continue")
    if guess >= 0:
        break
#FIXME: display guess
print(guess)

for i in range(10):
    print(i)
    if (i == guess):
        print('found')
        break
print("found", i)