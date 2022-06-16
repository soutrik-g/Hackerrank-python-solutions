if __name__ == '__main__':
    N = int(input())
    command = []
    for _ in range (N):
        command.append(input().split())
    final = []
    for i in range(len(command)):
        if(command[i][0] == "insert"):
            final.insert(int(command[i][1]), int(command[i][2]))
        elif(command[i][0] == "print"):
            print (final)
        elif(command[i][0] == "remove"):
            final.remove(int(command[i][1]))
        elif(command[i][0] == "append"):
            final.append(int(command[i][1]))
        elif(command[i][0] == "sort"):
            final.sort()
        elif(command[i][0] == "pop"):
            final.pop()
        elif(command[i][0] == "reverse"):
            final.reverse()
            
            
