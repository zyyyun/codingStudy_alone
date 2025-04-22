def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    
    for i in range(n):
        success = True
        for j in range(7):
            day_of_week = (startday + j - 1) % 7 + 1
            if day_of_week in [6,7]:
                continue
                
            wish_time = schedules[i]
            accepted_time = (wish_time // 100) * 100 + (wish_time % 100 + 10)
            if (accepted_time % 100 >= 60):
                accepted_time = ((accepted_time // 100 + 1) *100 + (accepted_time % 100 - 60))
            
            if timelogs[i][j] > accepted_time:
                success = False
                break
        if success:
            answer += 1
                
    return answer
