def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds
    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
        
    video_len_i = time_to_seconds(video_len)
    pos_i = time_to_seconds(pos)
    op_start_i = time_to_seconds(op_start)
    op_end_i = time_to_seconds(op_end)
    point = pos_i
    if(op_start_i <= point <= op_end_i):
        point = op_end_i
    
    for command in commands:
        if (command == "next"):
            point = point + 10
            if(point > video_len_i):
                point = video_len_i
        elif (command == "prev"):
            point = point - 10
            if (point < 0):
                point = 0
                
        if(op_start_i <= point <= op_end_i):
            point = op_end_i
            
        
    return seconds_to_time(point)