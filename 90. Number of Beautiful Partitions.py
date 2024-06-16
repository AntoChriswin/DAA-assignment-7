def count_beautiful_partitions(s, k, minLength):
    MOD = 10 ** 9 + 7
    primes = {'2', '3', '5', '7'}

    def is_prime(char):
        return char in primes

    def is_beautiful_partition(partition):
        if len(partition) < k:
            return False
        for i in range(k):
            if not is_prime(partition[i][0]) or is_prime(partition[i][-1]):
                return False
        return True

    def generate_partitions(s, start, path, partitions):
        if start == len(s):
            if len(path) == k:
                partitions.append(path[:])
            return
        for i in range(start, len(s)):
            if len(s[start:i + 1]) >= minLength:
                path.append(s[start:i + 1])
                generate_partitions(s, i + 1, path, partitions)
                path.pop()

    partitions = []
    generate_partitions(s, 0, [], partitions)

    count = 0
    for partition in partitions:
        if is_beautiful_partition(partition):
            count += 1

    return count % MOD


# Example Usage
s = "23542185131"
k = 3
minLength = 2
print(count_beautiful_partitions(s, k, minLength))  # Output: 3

s = "23542185131"
k = 3
minLength = 3
print(count_beautiful_partitions(s, k, minLength))  # Output: 1

s = "3312958"
k = 3
minLength = 1
print(count_beautiful_partitions(s, k, minLength))  # Output: 1
