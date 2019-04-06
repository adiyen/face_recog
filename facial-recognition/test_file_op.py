
def write_names():
    f = open("names.txt", "w")
    while True:
        name = input("Enter your name: ")
        if name == "q":
            break
        grade = input("whats your grade: ")
        school = input("school: ")
        
        f.write(name + "," + grade + "," + school + "\n")
    f.close()

def read_names():
    f = open("names.txt", "r")
    for line in f:
        name, grade, school = line.split(",")
        print(name, grade, school)
    f.close()


if __name__ == "__main__":
    oper = input("What do you want to do: r/w?")
    if oper == "r":
        read_names()
    elif oper == "w":
        write_names()
    else:
        raise ValueError("Select r or w")
