from timetable_database import *
print('		               WELCOME TO TIMETABLE MANAGER')
print('YOU CAN DO THE FOLLOWING OPERATIONS:')
print('YOU CAN MANAGE THE TIME TABLE OF CLASSES 10 TO 12')
print('1:ADD A PERIOD\n2:CHECK PERIOD\n3:UPDATE TIMETABLE \n4:DELETE A PERIOD\n5:EXIT')
r=True
while r:
    print('ENTER YOUR CHOICE: ')
    m=input()
    if m=='1' :
        try:
            a=int(input('ENTER CLASS:  '))
            b=input('ENTER   DAY:  ')
            q=w=e=l=t=y=u=f=o=''
            if a==12 or a==11:
                op=7
                for i in range (1,op):
                    print('ENTER SUBJECT FOR PERIOD:',i)
                    r=input()
                    if i==1:
                        q=i
                    if i==2:
                        w=r
                    if i==3:
                        e=r
                    if i==4:
                       l=r
                    if i==5:
                       t=r
                    if i==6:
                       y=r
               
                insert1211(a,b,q,w,e,l,t,y)
            elif a==10:
                op=9 
                for i in range (1,op):
                    print('ENTER SUBJECT FOR PERIOD:',i)
                    r=input()
                    if i==1:
                        q=r
                    if i==2:
                        w=r
                    if i==3:
                        e=r
                    if i==4:
                       l=r
                    if i==5:
                       t=r
                    if i==6: 
                       y=r
                    if i==7:
                       u=r
                    if i==8:
                       f=r
                    if i==9:
                       o=r
                insert10(b,q,w,e,l,t,y,u,f,o)

        except:
            print('ERROR IN QUERY TRY AGAIN!!!')
            
    
    elif m=='2' :
            print('ENTER WHAT YOU WANT TO SEE \n1:SEE TIMETABLE OF A CLASS\n2:SEE TIMETABLE OF A PARTICULAR DAY')
            c=input()
            if c=='1':
                z=int(input('ENTER CLASS:  '))
                if z==10:
                    show10()
                if z==11:
                    show11()
                if z==12:
                    show12()
            elif c=='2':
                z=int(input('ENTER CLASS: '))
                x=input('ENTER DAY: ')
                period(z,x)
        
    elif m=='3':
        try:
            print('ENTER CLASS: ')
            v=int(input())
            if v==12:
                a=input('ENTER DAY: ')
                d=input('ENTER PERIOD NUMBER: ')
                c=input('ENTER NEW PERIOD: ')
                update12(a,d,c)

            if v==11:
                a=input('ENTER DAY: ')
                d=input('ENTER PERIOD NUMBER: ')
                c=input('ENTER NEW PERIOD: ')
                update11(a,d,c)
            if v==10:
                a=input('ENTER DAY: ')
                d=input('ENTER PERIOD NUMBER: ')
                c=input('ENTER NEW PERIOD: ')
                update10(a,d,c)
        except:
            print('ERROR IN QUERY TRY AGAIN!!!')
    elif m=='4':
        try:
            print('ENTER CLASS: ')
            v=int(input())
            if v==12:
                a=input('ENTER DAY: ')
                delete12(a)
            if v==11:
                a=input('ENTER DAY: ')
                delete11(a)
            if v==10:
                a=input('ENTER DAY: ')
                delete10(a)
        except:
            print('ERROR IN QUERY TRY AGAIN!!!')
    elif m=='5':
        quit()
    print('\n\n')
    
    
