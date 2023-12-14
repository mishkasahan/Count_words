f = open('file1.txt',  'r', encoding= 'UTF-8')
count_words = len(f.read().split())
print(count_words)