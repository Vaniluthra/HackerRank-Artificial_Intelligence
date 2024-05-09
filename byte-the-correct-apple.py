def count_keywords(line, keywords):
    count = 0
    for word in line.split():
        if word.lower() in keywords:
            count += 1
    return count

def disambiguate(line):
    # Load keywords from text files
    with open('apple-computers.txt', 'r', encoding='utf-8') as f:
        computer_keywords = set(f.read().lower().split())
    with open('apple-fruit.txt', 'r', encoding='utf-8') as f:
        fruit_keywords = set(f.read().lower().split())
    
    # Count occurrences of keywords in the line
    computer_count = count_keywords(line, computer_keywords)
    fruit_count = count_keywords(line, fruit_keywords)
    
    # Determine the topic based on keyword counts
    if computer_count > fruit_count:
        return 'computer-company'
    elif fruit_count > computer_count:
        return 'fruit'
    else:
        return 'undetermined'

# Read input
N = int(input())
lines = [input() for _ in range(N)]

# Perform disambiguation for each line and print the result
for line in lines:
    print(disambiguate(line))
