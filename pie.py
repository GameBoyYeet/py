pieflavor = input("What's your favorite pie flavor?\n")
pieflavor.lower()
for pieflavor in ["e", "pumpkin", "apple", "pie"]:
    match pieflavor:
        case "e":
            print("interesting flavor")
            break;
        case "pumpkin":
            print("tasty")
            break;
        case "apple":
            print("tastee but hav never tryd")
            break;
        case "pie":
            print("PIE FLAVOR")
            break;
        case _:
            print("What")
            break