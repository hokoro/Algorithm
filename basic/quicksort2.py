array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료 -> 정렬을 할 필요가 없기 때문에
        return

    pivot = start  # 피벗의 첫번째 원소 를 지정 ( 위치는 상관 없다)
    left = start + 1  # 왼쪽을 start 에서 한칸 옆에 있는 원소
    right = end  # 제일 오른쪽 있는 원소를 right 로 설정

    while left <= right:  # 왼쪽이랑 오른쪽이 교차 하기 전까지 반복문을 수행
        # 피벗보다 큰데이터를 찾을때
        while left <= end and array[left] <= array[pivot]:
            left += 1  # 피벗의 위치를 설정 해야 하기 때문에
        while right > start and array[right] >= array[pivot]:
            right -=1

        if(left > right): # left 와 right 가 교차 하면
            array[right] , array[pivot] = array[pivot],array[right]

        else:
            array[left] , array[right] = array[right] , array[left]

        print(f'정렬 : {array}')

        quick_sort(array,start,right-1) # 피벗을 기준으로 왼쪽
        quick_sort(array,right+1,end) # 피벗을 기준으로 오른쪽



quick_sort(array,0,len(array)-1)