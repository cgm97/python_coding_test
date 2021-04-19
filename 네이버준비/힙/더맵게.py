# def solution(scoville, K): 처음에 직접 짜본 코드 -> 시간이 오래 걸림
#     result = 0
#     count = 0
#     while True :
#         scoville.sort()
#         if result > K :
#             break
#         else :
#             result = scoville[0] + (scoville[1] * 2)
#             scoville.pop(0)
#             scoville.pop(1)
#             scoville.append(result)
#             count += 1
#     return count


import heapq # 시간 효율을 위해 heap 을 사용 해봄 - 힙은 자동 정렬 해줌
def solution(scoville, K):
    heap = []
    count = 0
    for i in scoville :
        heapq.heappush(heap,i)
    while 1 :
        if heap[0] < K and len(heap) <= 1 : # 예외상황 -> 기준의 맵기가 안될때
            count = -1
            break
        if heap[0] >= K :
            break
        heapq.heappush(heap,heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        count += 1
    return count
