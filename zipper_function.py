def zipper(listA, listB):
    zipped = zip(listA, listB)

    return zipped

if __name__ == '__main__':
    food = ['pizza', 'sushi', 'jam']
    people = ['Bob', 'Kevin', 'Angela']

    first_item = zipper(food, people)
    for item in result:
        print(item)
