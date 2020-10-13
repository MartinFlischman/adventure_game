print("Welcome to my adventure game!🎮")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print("You may play the game!")

    wants_to_play = input("Do you want to play? (Y/n) ").lower()
    if wants_to_play == "y":
        print("You are starting with", health, "health points.")
        print("Let's play!🙂")

        left_or_right = input(
            "First choice... Do you go Left or Right? (left/right) ")
        if left_or_right == "left":
            ans = input("You follow the path and reach a river... Do you swim across or walk over the bridge? (swim/walk) ")

            if ans == "swim":
                print("You swim across the river. You loose 0 health points.")
                health -= 0

            elif ans == "walk":
                print("You walk across the old bridge. You step right through the rotton wood and hurt your leg. You loose 5 health points.")
                health -= 5

            ans = input("You notice a house and a cave. Which do you go to? (house/cave) ")
            if ans == "house":
                print("You go into the house, wake up, and realise you were dreaming. You don't loose any health points and win the game.")
                health -= 0

                if health <= 0:
                    print("You now have 0 health points and loose the game.")
                else:
                    print("You have survived... You win!")

            else:
                print("You go into the cave and a bear attacks you. You die and loose the game.")

        else:
            print("You fell down the stairs and die. You lose! ⚰️...")

    else:
        print("You lose. Goodbye!😒")
else:
    print("You are not old enough to play the game.🚫")
