# Brute Force
def brute_force():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

# Using step parameter


def using_step():
    for i in range(0, 101, 2):
        print(i)


print('brute force')
brute_force()

print('using step')
using_step()
