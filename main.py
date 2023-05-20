# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def question1(s):
    temp = list(s)
    ans = temp[::-1]
    return ans


def question2(s):
    temp = list(s.split())
    # print(temp)
    test = ''
    for i in temp:
        test += i[::-1]
    return test


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q1 = question1("junyiacademy")
    answer = ""
    for i in q1:
        answer += i
    print("question 1 answer:", answer)

    print("question 2 answer:", question2("flipped classroom is important"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
