f=open('data.txt','w')

wrong=1
while wrong==1:
    wrong=0
    fnr=input("Type in your phone full phone number (with the prefix separated by a space): ")

    sep=fnr.find(' ')
    pfx=fnr[:sep]
    nr=fnr[sep+1:]

    if len(fnr)>14 or len(fnr)<9:
        print("\n!!!!! Phone number doesn't exist !!!!!\n")
        wrong=1

    with open('prefixes.txt') as file:
        contents=file.read()
        if pfx in contents:
            continue
        elif wrong!=1:
            print("\n!!!!! Phone number doesn't exist !!!!!\n")
            wrong=1

wrong=1
while wrong==1:
    wrong=0

    email=input("Type in your email: ")

    sep=email.find('@')
    if sep==-1:
        wrong=1
        print("\n!!!!! Email isn't valid !!!!!\n")
    else:
        user=email[:sep]
        domain=email[sep+1:]

    sep=domain.find('.')
    if sep==-1:
        if wrong!=1:
            print("\n!!!!! Email isn't valid !!!!!\n")
            wrong=1
    else:
        ext=domain[sep+1:]
        if ext=="":
            if wrong!=1:
                print("\n!!!!! Email isn't valid !!!!!\n")
                wrong=1

f.write(fnr+" | "+email+'\n')
