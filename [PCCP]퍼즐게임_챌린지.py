def solution(diffs, times, limit):
    # 이진 탐색을 위한 함수 정의
    def can_solve(level):
        total_time = 0
        prev_time = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            
            if diff <= level:
                # 틀리지 않은 경우
                total_time += time_cur
            else:
                # 틀린 경우
                mistakes = diff - level
                total_time += mistakes * (time_cur + prev_time) + time_cur
            
            # 이전 퍼즐의 소요 시간 저장
            prev_time = time_cur
            
            # 제한 시간을 초과하면 False
            if total_time > limit:
                return False
        
        return True

    # 이진 탐색으로 숙련도의 최적값을 찾기
    left, right = 1, max(diffs)  # 숙련도의 범위
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_solve(mid):
            # 제한 시간 내에 풀 수 있으면 더 낮은 숙련도를 탐색
            result = mid
            right = mid - 1
        else:
            # 제한 시간 내에 풀 수 없으면 숙련도를 높여야 함
            left = mid + 1
    
    return result
