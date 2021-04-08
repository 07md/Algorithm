if __name__ == '__main__':
    ans = 0
    for i in range(1, 2021):
        ans += str(i).count('2')
    print(ans)
