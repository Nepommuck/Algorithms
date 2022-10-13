from cgi import test


def fill_strict(text, names):
    best_i = -1
    best_name = ""
    for i in range(len(names)):
        l = len(names[i])
        if l > len(best_name) and l <= len(text) and text[:l] == names[i]:
            best_i = i
            best_name = names[i]

    return best_i

def fill_at(text, j, names):
    let = text[j]
    # print(let)

    best_ind = -1
    best_score = 0
    for i in range(len(names)):

        # Searching for the last fitting letter but in the way that name won't start earlier than text 
        for k in range(0, min(len(names[i]), j + 1)):

            # Checking if letters correspond and word won't be longer than text
            if len(text) - j >= len(names[i]) - k and names[i][k] == let:

                ok = True
                for m in range(len(names[i])):
                    if names[i][m] != text[j - k + m]:
                        ok = False
                        break
                if ok:

                    # Updating the best score
                    if len(names[i]) - k > best_score:
                        best_score = len(names[i]) - k
                        best_ind = i
                    break
    
    return best_ind, best_score


def f(t, s):
    used = fill_strict(t, s)
    outp = []

    if used < 0:
        print("-1")
        return    

    outp.append(str(used + 1) + ' 1')
    # print(used + 1, 1)

    # print("We used", s[used])
    ind = len(s[used])
    # print("We are at", ind)

    while(ind < len(t)):
        # print('Akt ind:', ind)
        used, przes = fill_at(t, ind, s)
        if used < 0:
            print("-1")
            return    

        # print("We used", s[used])
        # print(used + 1, ind + przes - len(s[used]) + 1)
        outp.append(str(used + 1) + ' ' + str(ind + przes - len(s[used]) + 1))

        ind += przes
        # print("We are at", ind)
    
    print(len(outp))
    for line in outp:
        print(line)   
        

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):

        t = input()
        n = int(input())
        s = []
        for _ in range(n):
            s.append(input())
        
        f(t, s)
