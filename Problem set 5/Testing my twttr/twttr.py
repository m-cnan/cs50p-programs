def main():
    print(shorten(input("Input: ")))


def shorten(word):
    twttr=""
    for x in word:
        if x not in ["A","a","E","e","I","i","O","o","U","u"]:
            twttr=twttr+x
    return twttr



if __name__ == "__main__":
    main()