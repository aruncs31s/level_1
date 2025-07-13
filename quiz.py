#!/usr/bin/env python3

"""
If you found self here , this a just a python script using only the print and input functions.
"""
score = 0
count = 0


def main():

    global score
    global count
    print("Level 1".center(50, "="))
    print()

    should_continue = input("Did you finish reading README (y/N): ").lower().strip()

    if should_continue not in ["y", "yes"]:
        print("Please read the README".center(50))
        return
    score += 1
    count += 1
    print(f"\nScore {score} / {count}")

    print("Question 1:")
    print("Imagine you are told to clone a GitHub repo.")
    print("Which command would you use to clone a GitHub repo?")
    print()

    ans_1 = input("Please enter the command: ").lower().strip()

    if ans_1 not in ["git clone", "clone"]:
        print("Incorrect! Please read level_0 again.")
        return

    print("Correct!")
    score += 1
    count += 1
    print(f"Score {score} / {count}")
    print()

    print("Question 2:")
    ans_2 = input("Who created Git? ").lower().strip()

    if ans_2 not in ["linus torvalds", "linus", "torvalds"]:
        print("Incorrect! Please READ the README.")
        return

    print("Correct!")
    score += 1
    count += 1
    print(f"\nScore {score} / {count}")
    print()

    print("Question 3:")
    print("Imagine you've released software with version v0.1.0.")
    print("After some time, you made changes and fixes - all minor changes.")
    print("In total, you made 7 minor changes, pushing each change to GitHub.")
    print()

    ans_3 = input("What will be the current version number: ").lower().strip()

    if ans_3 not in ["v0.8.0"]:
        print("Incorrect! Read the README again.")
        return

    print("Correct!")
    score += 1
    count += 1
    print(f"\nScore {score} / {count}")
    print()
    print("You will find the hints for next level in a folder .hidden".center(50, "="))


if __name__ == "__main__":
    main()
