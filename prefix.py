word = str(input())

prefix = word[0] + word[1] + word[2]
w_length = len(word) - 3
suffix = word[w_length]+ word[w_length + 1] + word[w_length + 2]


print('Prefix: {}'.format(prefix))
print('Suffix: {}'.format(suffix))
