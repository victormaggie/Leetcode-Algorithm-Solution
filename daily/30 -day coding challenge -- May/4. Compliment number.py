classs Solution:
    def compliment(num):
        bit_count = 0
        n = num
        while n > 0:
            bit_count += 1
            n = n >> 1

        all_bits_set = pow(2, bit_count) - 1

        return num ^ all_bits_set

# time complexity o(b)
# space complexity o(1)