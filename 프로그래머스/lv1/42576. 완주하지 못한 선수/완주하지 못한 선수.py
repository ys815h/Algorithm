# 완주하지 못한 사람을 return
# 참여자 명단엔 중복된 이름이 있을 수 있다
# 효율성을 고려한 접근방법
# for문을 돌려 값이 다른거 찾으면 return 시키고 break
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
        
