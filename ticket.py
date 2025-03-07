# args && kwargs

def userdetails(*args):
    print(args)

userdetails('mohith', 25, 'India', 'telugu', 5392)

#################################

def userdetails1(**kwargs):
    print(kwargs)

userdetails1(Name='mohith', age=25, country='India', lang='telugu', ID=5392)

#########################################

def userdetails2(**kwargs):
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))
    
userdetails2(Name='mohith', age=25, country='India', lang='telugu', ID=5392)

#############################################

def UserDetails3(licenseNo, *args , phoneNo=0 , **kwargs): # Using all arguments
    print('License No :- ', licenseNo)
    j=''
    for i in args:
        j = j+i
    print('Full Name :-',j)
    print('Phone Number:- ',phoneNo)
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))

name = ['mohith', ' ','reddy']
mydict = {'Name': 'mohith', 'age': 25, 'country': 'India', 'lang': 'telugu', 'ID': 5392}

UserDetails3('BHT145' , *name , phoneNo=1234567890,**mydict )
