n=int(input("Enter the number of email adresses: "))
for i in range(0,n):
    str1=input("Enter your email: ")
    def mailslicer(str1):
        x=str1.split("@")
        userName=x[0]
        domainName=x[1]
        b=domainName.upper()
        print("userName:",userName,"and","domainName:",b)
    mailslicer(str1)
