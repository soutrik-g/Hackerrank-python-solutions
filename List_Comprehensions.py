if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_for_x = [a for a in range (0,x)]
    list_for_y = [b for b in range (0,y)]
    list_for_z = [c for c in range (0,z)]
    answer_list = []
    for i in range (0,len(list_for_x)):
        for j in range (0,len(list_for_y)):
            for k in range (0,len(list_for_z)):
                if (list_for_x[i]+list_for_y[j]+list_for_z[k]!= n):
                    answer_list.append([list_for_x[i],list_for_y[j],list_for_z[k]])
                    print(answer_list)
