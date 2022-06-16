if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = set(arr)
    new_arr = sorted(new_arr)
    print(new_arr[len(new_arr)-2])
