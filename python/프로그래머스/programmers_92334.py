def solution(id_list, report, k):
    
    
    banner_list = []
    banned_list = []
    report_data = []
    report = set(report)
    report = list(report)
    for report_element in report:
        #신고자 , 신고 당한 사람
        banner, banned = report_element.split(" ")
        banner_list.append(banner)
        banned_list.append(banned)
        report_data.append({banner : banned})
        print(banner_list) , print(report_data)
    
    for id in id_list:
        # if ()
    
    answer = []
    return answer