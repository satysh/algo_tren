N, K = map(int, input().split())
car_nums = list(map(int, input().split()))

car_nums_prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    car_nums_prefix_sum[i] = car_nums_prefix_sum[i - 1] + car_nums[i - 1]

left = rigth = 0
count = 0
while rigth != len(car_nums_prefix_sum):
    cur_slice_sum = car_nums_prefix_sum[rigth] - car_nums_prefix_sum[left]
    if cur_slice_sum < K:
        rigth += 1
    elif cur_slice_sum > K:
        left += 1
    elif cur_slice_sum == K:
        count += 1
        rigth += 1
        left += 1

print(count)

