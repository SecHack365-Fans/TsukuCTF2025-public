import os
import secrets
import signal

FLAG = os.getenv("FLAG", "TsukuCTF25{dummy_flag}")

class xor_tsuku_shift:
    def __init__(self, seed):
        self.a = seed

    def shift(self):
        self.a ^= (self.a << 17) & 0xFFFFFFFFFFFFFFFF
        self.a ^= (self.a >> 9) & 0xFFFFFFFFFFFFFFFF
        self.a ^= (self.a << 18) & 0xFFFFFFFFFFFFFFFF
        return self.a & 0xFFFFFFFFFFFFFFFF

def janken(a, b):
    return (a-b+3) % 3

rng = xor_tsuku_shift(seed=secrets.randbits(64))

signal.alarm(600)

print("Tsukushi: Let's play janken!")
print("Tsukushi: Win 294 times in a row and you'll get the flag.")

for challenge in range(300):
    print(f"Tsukushi: You have {300-challenge:03} tries.")
    for round in range(294):
        print(f"--- Round {round:03} ---")
        tsukushi = rng.shift()
        you = int(input("Rock, Paper, Scissors... Go! (Rock: 0, Paper: 1, Scissors: 2): "))

        if you != 0 and you != 1 and you != 2:
            print("Tsukushi: Hey, you cheated!")
            break 

        result = janken(you, tsukushi)

        if result == 1:
            print("Tsukushi: You win!")
            if round != 293:
                print("Tsukushi: Let's go to the next round!")
        elif result == 0:
            print("Tsukushi: Draw! ...But If you wanna get the flag, you have to win 294 rounds in a row.")
            break
        else:
            print("Tsukushi: You lose!")
            break

    else:
        print("Tsukushi: You won 294 times in a row?! That's incredible!")
        print(f"Tsukushi: So, here is the flag. {FLAG}")
        quit()

else:
    print("Tsukushi: GGEZ, Bye!")
