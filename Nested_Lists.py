if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    ordered_scores = sorted(list(set([info[1] for info in record])))
    second_lowest_score = ordered_scores[1]
    list_of_names = []    
    for info in record:
        if(info[1] == second_lowest_score):
            list_of_names.append(info[0])
    list_of_names.sort()
    for name in list_of_names:
        print(name)
