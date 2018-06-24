for i in range(-10,10):
    for j in range(-10,10):
        print("number A: {} : {}, number B:{} : {}, added {} : {}".format(i,bin(i),j,bin(j),i^j,bin(i^j)))
