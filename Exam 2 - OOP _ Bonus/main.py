from Cat import Cat
from Fish import Fish
from Spider import Spider


if __name__ == '__main__':
    # Testing the Animal class
    print("----------------------------------------------- Start -----------------------------------------------")
    print("Testing Animal class:\n")

    # Create Animals
    cat1 = Cat("Kitty")
    fish1 = Fish("Nemo")
    spider1 = Spider("Spiderman")

    # Print Animals
    print(f" - Cat 1: {cat1}\n")
    print(f" - Fish 1: {fish1}\n")
    print(f" - Spider 1: {spider1}\n")

    # Testing Cat methods
    print("Testing Cat methods:\n")
    print(f"Cat's name: {cat1.getName()}")
    cat1.setName("Whiskers")
    print(f"Cat's new name: {cat1.getName()}")
    cat1.play()
    cat1.eat()
    cat1.walk()
    print()

    # Testing Fish methods
    print("Testing Fish methods:\n")
    print(f"Fish's name: {fish1.getName()}")
    fish1.setName("Goldie")
    print(f"Fish's new name: {fish1.getName()}")
    fish1.play()
    fish1.eat()
    fish1.walk()
    print()

    # Testing Spider methods
    print("Testing Spider methods:\n")
    print(f"Spider's name: {spider1.getName()}")
    spider1.setName("Webster")
    print(f"Spider's new name: {spider1.getName()}")
    spider1.play()
    spider1.eat()
    spider1.walk()
print("----------------------------------------------- End -----------------------------------------------")

