# For Loop with Range

for number in range (1, 11, 3):
    print(number)


print("Number Pattern")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # run inner loop i+1 times
    for j in range (1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")