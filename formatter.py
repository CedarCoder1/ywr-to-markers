with open("input.txt", "r") as file:
    text = file.read()
    
    # Do the lines
    for line in text.splitlines():
        if line.find("PositionX") != -1:
            print()
        else:
            print(line.split(",")[0] + "," + line.split(",")[1] + "," + line.split(",")[2])
            
input() # Keeps the terminal open.