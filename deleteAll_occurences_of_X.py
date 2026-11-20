def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
    # Write your solution here
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==X:
            arr.pop(i)
            arr.append(0)
   
    return arr
    pass
