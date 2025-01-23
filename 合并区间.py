intervals = eval(input())
intervals.sort(key=lambda x: x[0])
start = intervals[0][0]
end = intervals[0][1]
length = end - start
for i, j in intervals[1:]:
    if j <= end:
        continue
    elif j > end and i <= end:
        length += j - end
        end = j
    elif i > end:
        start = i
        end = j
        length += end - start
print(length)
#[[1,3],[2,6],[8,10],[15,18]]
#10

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    result = []
    length = end - start
    for i, j in intervals[1:]:
        if j > end:
            if i <= end:
                length += j - end
            else:
                result.append([start, start + length])
                start = i
                end = j
                length = j - i
    result.append([start, start + length])
    return result
