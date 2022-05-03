#--> Montgomery-Ladder
#-> The Montgomery-Ladder calculates the Output of the operation: "x = a^k" in a finite field and in a fixed amount of time, to prevent side-channel attacks
#-> Input: a, k, mod


def MontLadder(a, k, mod):
    # Formatting exponent k into a binary number
    k_bin = format(k, 'b')


    # Initializing x and y
    x = 1
    y = a % mod


    # Loop 
    for i in range(len(k_bin)):
        if k_bin[i] == "0":
            y = (x * y) % mod
            x = pow(x, 2, mod)
        elif k_bin[i] == "1":
            x = (x * y) % mod
            y = pow(y, 2, mod)
        print(str(len(k_bin) - i - 1), ": x = ", str(x) + "; y = ", str(y))

# Output: x
    print("x = a^k =  " + str(x))


# Input:
try: # a
        print("\nPlease enter a valid Integer: ")
        a = int(input("a: "))
except Exception as e:
        print("\nError: ", e)

try: # k
        print("\nPlease enter a valid Integer: ")
        k = int(input("k: "))
except Exception as e:
        print("\nError: ", e)

try: # mod
        print("\nPlease enter a valid Integer: ")
        mod = int(input("mod: "))
except Exception as e:
        print("\nError: ", e)


# Calling the function
MontLadder(a, k, mod)