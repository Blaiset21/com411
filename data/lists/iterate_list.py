def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    list = directions()
    for index in range(len(list)):
        print(f"{index}: {list[index]}")


def run():
    menu()


if __name__ == "__main__":
    run()