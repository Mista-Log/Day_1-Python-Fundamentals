def main():
    print("You find yourself standing at the edge of a dense, mysterious forest. A winding path disappears into the undergrowth. Do you:")
    print("1. Enter the forest")
    print("2. Turn back")
    choice = input("Choose your action: ")

    if choice == "1":
        print("You step onto the path and disappear into the forest. The air is thick with the scent of pine and damp earth. As you walk deeper, the trees seem to close in around you, creating a tunnel of darkness.")
        print("Suddenly, you hear a rustling in the bushes. Do you:")
        print("1. Investigate")
        print("2. Keep walking")
        choice = input("Choose your action: ")

        if choice == "1":
            print("As you approach the bushes, a small, furry creature emerges. It's a mischievous-looking fox with bright, curious eyes. The fox seems unafraid and even approaches you, sniffing your hand.")
            print("Do you:")
            print("1. Pet the fox")
            print("2. Back away")
            choice = input("Choose your action: ")

            if choice == "1":
                print("You gently pet the fox, and it purrs contentedly. A sense of peace washes over you as you interact with the wild creature.")
            elif choice == "2":
                print("You hesitate, unsure whether to trust the fox. As you back away, it scampers off into the undergrowth.")
        elif choice == "2":
            print("You decide to ignore the rustling and continue your journey. As you walk further, the forest becomes even more dense and the path becomes narrower.")

    elif choice == "2":
        print("You turn back, deciding the forest is too dangerous. As you walk away, you can't shake the feeling that you're missing out on something.")

    else:
        print("Invalid choice. Please enter 1 or 2.")
        