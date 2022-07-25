def solution(id_list, report, k):
    report_data = {id : 0 for id in id_list}
    #id_list의 길이만큼 0으로 초기화
    answer = [0 for i in range(len(id_list))]
    
    for report_item in set(report):
        #신고자 , 신고 당한 사람
        banner, banned = report_item.split(" ")
        report_data[banned] += 1

    for report_item in set(report):
        banner,banned = report_item.split()
        if report_data[banned] >= k:
            answer[id_list.index(banner)] += 1

            
    return answer