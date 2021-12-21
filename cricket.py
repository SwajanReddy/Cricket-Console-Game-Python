import random
def toss(x,y):
    bat1=str()
    print('toss time')
    who=int(input('who say the toss--1:p1n or 2:p2n:'))
    if who==1:
        choice=int(input('1:heads or 2:tails--'))
        tos=random.randint(1,2)
        print(tos)
        if choice==tos:
            choose=int(input('p1 you won the toss,1:batting or 2:bowling--'))
            if choose==1:
                print(x,'you are batting now')
                bat1=bat1+"p1"
            elif choose==2:
                print(x,'you are bowling now')
                bat1=bat1+"p2"
        else:
            print(x,'you loss the tose')
            choose=int(input('p2 whats your choice,1:batting or 2:bowling--'))
            if choose==1:
                print(y,'you are batting now')
                bat1=bat1+"p2"
            elif choose==2:
                print(y,'you are bowling now')
                bat1=bat1+"p1"
    else:
        choice=int(input('1:heads or 2:tails--'))
        tos=random.randint(1,2)
        print(tos)
        if choice==tos:
            #print(tos)
            choose=int(input('p2 you won the toss,1:batting or 2:bowling--'))
            if choose==1:
                print(y,'you are batting now')
                bat1=bat1+"p2"
            elif choose==2:
                print(y,'you are bowling now')
                bat1=bat1+"p1"
        else:
            print(y,'you loss the tose')
            choose=int(input('p1 whats your choice,1:batting or 2:bowling--'))
            if choose==1:
                print(x,'you are batting now')
                bat1=bat1+"p1"
            elif choose==2:
                print(x,'you are bowling now')
                bat1=bat1+"p2"
    #print(bat1)
    return bat1
def bat(x):
    score=0
    print(x,'your innings,allowed runs are 1,2,3,4,6')
    alruns=[1,2,3,4,6]
    willing=True
    wickets=0
    overs=0
    ball=0
    while willing and overs<=5:
        bowl=random.choice(alruns)
        batting=int(input('enter runs:-'))
        if batting in alruns:
            ball=ball+1
            if ball>6:
                overs=overs+1
                ball=ball-6
            if batting!=bowl:
                print('bowl is',bowl)
                score=score+batting
                print('score=',score,'-',wickets,'(',overs,'.',ball,')')
                if score==50:
                    print('congrants',x,'for the 50')
                if score==100:
                    print('excellent century master scored',score)
            elif batting==bowl:
                wickets=wickets+1
                print('bowl is also',bowl,'you are out')
                #print('score=',score,'-',wic)
                print('score=',score,'-',wickets,'(',overs,'.',ball,')')
                if score<100 and score>90:
                    print('missed a well deserved century')
                if wickets==3:
                    willing=False
        else:
            print(batting,'is not allowed runs,try again')
    #print(score)
    print('your innings up')
    return score
def checkwin(pp1,pp2,p1n,p2n):
    if pp1>pp2:
        print(p1n,'is winner.Won by',(pp1-pp2),'runs')
    elif pp1==pp2:
        print('its  a tie')
    else:
        print(p2n,'won by',(pp2-pp1),'runs')
def bat2(x,tar):
    score=0
    print(x,'your innings,allowed runs are 1,2,3,4,6')
    alruns=[1,2,3,4,6]
    willing=True
    wickets=0
    overs=0
    ball=0
    while willing and (score<=tar) and overs<=5:
        bowl=random.choice(alruns)
        batting=int(input('enter runs:-'))
        if batting in alruns:
            ball=ball+1
            if ball>6:
                overs=overs+1
                ball=ball-6
            if batting!=bowl:
                print('bowl is',bowl)
                score=score+batting
                #print('score=',score,'-',wickets)
                print('score=',score,'-',wickets,'(',overs,'.',ball,')')
                if score<tar:
                    print('more',(tar-score),'to win')
                if score==50:
                    print('congrants',x,'for the 50')
                if score==100:
                    print('excellent century master scored',score)
            elif batting==bowl:
                wickets=wickets+1
                print('bowl is also',bowl,'you are out')
                #print('score=',score,'-',wickets)
                print('score=',score,'-',wickets,'(',overs,'.',ball,')')
                if score<100 and score>90:
                    print('missed a well deserved century')
                if wickets==3:
                    willing=False
        else:
            print(batting,'is not allowed runs,try again')
    #print(score)
    print('your innings up')
    return score
def play():
    print('hello,welcome to python cricket game protocol by SWAJAN_AURNAV')
    p1n=input('enter p1 name:')
    p2n=input('enter p2 name:')
    pp1=0
    pp2=0
    #toss(p1n,p2n)
    if toss(p1n,p2n)=='p1':
        #bat(p1n)
        pp1=bat(p1n)
        print(p1n,'your score is',pp1)
        print(p2n,'your target is',(pp1+1))
        #bat(p2n)
        print(p2n,'your score is',pp2)
        pp2=bat2(p2n,(pp1+1))
        checkwin(pp1,pp2,p1n,p2n)
    else:
        #bat(p2n)
        pp2=bat(p2n)
        print(p2n,'your score is',pp2)
        print(p1n,'your target is',(pp2+1))
        #bat(p1n)
        print(p1n,'your score is',pp1)
        pp1=bat2(p1n,(pp2+1))
        checkwin(pp1,pp2,p1n,p2n)
    #bat()
    #thanks()
    print('-----------------------------games up---------------------------------------')
play()

