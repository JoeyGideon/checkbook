with open('balance.txt', 'r') as f:
    balance = float(f.read().strip())

    while True:
        print('\nWhat would you like to do?')
        print('1) View current balance')
        print('2) Record a debit *purchase')
        print('3) Record a credit *deposit')
        print('4) EXIT ')

        #prompt for user input
        choice = input()
        if choice == '1':
        #Display current balance
            print('Your current balance is ${:.2f}'.format(balance))

        elif choice == '2':
        # record a debit
            amount = input('Enter the debit amount:')
            if amount.isdigit():
                amount = float(amount)
                balance -= amount
                with open('balance.txt','w') as f:
                    f.write(str(balance))
                print('Debit of ${:.2f} recorded! Your new balance is: ${:.2f}'.format(amount, balance))
            else:
                print('Please enter a valid amount!')

        elif choice == '3':
        #record a credit
            amount = input('Enter the credit amount:')
            if amount.isdigit():
                amount = float(amount)
                balance += amount
                with open('balance.txt', 'w') as f:
                    f.write(str(balance))
                print('Credit of ${:.2f} recorded! Your new balance is: ${:.2f}'.format(amount, balance))
            else:
                print('Please enter a valid amount!')

        elif choice == '4':
        # exit print3
        #  salutations
            print('Have a GREAT day!')
            break

        else:
            print('Invalid input. Please re-enter your choice!')


