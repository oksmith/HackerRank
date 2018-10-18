if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    
    N = len(students)
    scores = sorted(set([students[x][1] for x in range(N)]))
    second_lowest = [students[x][0] for x in range(N) if students[x][1] == scores[1]]
    second_lowest.sort()
    
    for s in second_lowest:
        print(s)
    
    
