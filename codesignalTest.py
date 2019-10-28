def luckyKids(behaviors):
    count = [0 for x in range (len(behaviors))]
    gift = 0
    for i in range(0,len(behaviors)):
        for j in range(0,len(behaviors) - 1 -i):
            if behaviors[i] > behaviors[j+1+i]:
                count[i] += 1
        if count[i] >= ((len(behaviors) - 1 - i )/2):
            gift += 1
    return gift


if __name__ == "__main__":
    luckyKids([7, 11, 10, 9, 5, 7, 5, 7, 6, 6, 6, 2])
