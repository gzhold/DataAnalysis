


fp = open("./../data/nativeBayes/stopword.txt")


stop_words = [line.strip().encode('utf-8').decode('utf-8') for line in fp.readlines()]

print(stop_words)
