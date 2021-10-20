u=['SauR','LnB','Sapna','Abhi','Kushal']
p=[111,222,333,444,555]
amt=[1000,2000,3000,4000,5000]

def login():
    ui=input('enter username')
    r = ui in u
    print(r)
    if(r==True):
        print('username is available')
        up=int(input('enter the password'))
        ind=u.index(ui)
        if(up==p[ind]):
            print('welcome')
            cash=amt[ind]
            print("enter the choice:-\n1=Withdraw\n2=Deposit\n3=check balance\n4=change pin\n5=exit")
            n=input("\nEnter the choice")
            #withdraw your amount
            if(n == '1'):
                
                print(f"Available cash in your bank account:{cash}")
                a=int(input("enter the amount that you want to withdraw:"))
                if(a>cash):
                    print("sorry available balance is low")
                
                else:
                    amt[ind]=cash-a
                    print(f"Cash you withdraw is={a}")
                    print(f"Available balance is={amt[ind]}")

            elif(n=="2"):
                deposit=int(input("Enter the amount that you want to deposit..\n"))
                amt[ind]=cash+deposit
                print(f"Available balance in your account is={amt[ind]}")
            elif(n=="3"):
                print(f"Your account balance is={amt[ind]}")
            
            elif(n=="4"):
                new_pass=int(input("enter your new password"))
                p[ind]=new_pass
                print("Your password is changed successfully")
            elif(n=="5"):
                exit()
            else:
                print("Please enter the correct choice and login again")

                    
            #deposit the amount
            #check balance
            #change your pin/password
        else:
            print('password is invalid')
    else:
        print('user is invalid')
def signup():
    ui=input('enter new username')
    up=int(input('enter new password'))
    u.append(ui)
    p.append(up)

while(1):
    op=int(input('1.login \n2.signup \n'))
    if(op==1):        
        login()
    elif(op==2):
        signup()
 
