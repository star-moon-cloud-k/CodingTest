def solution(id_list, report, k):
    banner_list = []
    banned_list = []
    #id_list의 길이만큼 0으로 초기화
    answer = [0 for i in range(len(id_list))]
    
    report = set(report)
    report = list(report)
    for report_element in report:
        #신고자 , 신고 당한 사람
        banner, banned = report_element.split(" ")
        banner_list.append(banner)
        banned_list.append(banned)
    
 
    
    #신고당한 id 수가 k보다 많은 경우 같은 인덱스에 k값, 아닌 경우 0
    
    for id in id_list:
        index = 0
        if (k <= banned_list.count(id)):
            for banned in banned_list:
                if (id == banned):
                    answer[id_list.index(banner_list[index])] += 1
                index += 1
                
    return answer