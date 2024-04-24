def solution(numbers):
    answer = []
    num = 0
    if(len(numbers) >2):
        for i in range(0, len(numbers)):
            for j in range(i+1,len(numbers)):
                answer.append(numbers[i]+numbers[j])
    else:
        answer.append(numbers[0] + numbers[1])
        
    answer = list(set(answer))
    answer.sort()
    return answer