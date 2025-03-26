users = {
    '1001': bankaccount('1001', 'abhishek', 'pass123', 1000),
    '1002': bankaccount('1002', 'kalyan', 'pass456', 2000),
    '1003': bankaccount('1003', 'manish', 'pass789', 3000)
}


def display(self):
    print(f"your balance = {self.bal}")

acc_holder=input("enter full name:")
acc_no=input("enter account number: ")
pass_wrd=input('password:')

if acc_no in users and users[acc_no].pass_wrd == pass_wrd and users[acc_no].acc_holder==acc_holder:
    acc = users[acc_no]
    print(f"Welcome to BanK Mr/Mrs.{acc.acc_holder}\n")
    print('exit before leave')
else:
    print("Invalid account number or password \nIllegal user  ")
    exit()
