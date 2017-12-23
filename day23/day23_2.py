# after some heavy looking, the program "obviously" checks composite numbers

def is_prime(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

# read from input
b = 109300
c = 126300

count = 0
for n in range(b,c+1,17):
    if not is_prime(n):
        count += 1

print("Part 2:", count)