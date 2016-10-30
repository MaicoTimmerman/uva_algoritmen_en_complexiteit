# For a ascii triangle calculate the maximum path value
def solve(triangle):
    while len(triangle) > 1:
        # Pop the last to rows
        last_row = triangle.pop()
        second_last_row = triangle.pop()
        triangle.append([max(last_row[i], last_row[i+1]) + t \
                for i,t in enumerate(second_last_row)])
    return triangle[0][0]

# Load in the triangle
data = [list(map(int, row.strip().split())) \
       for row in [line.strip() \
       for line in open('triangle.txt')]]
print(data)
print('max: ' + str(solve(data)))

