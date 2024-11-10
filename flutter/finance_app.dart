import "dart:io";

// option 1
// class BankAccount {
//   String accountNum;
//   String holderName;
//   double balance;
//   String accountType;

//   BankAccount(this.accountNum, this.holderName, this.balance, this.accountType);

//   void deposite(double amount) {
//     balance += amount;
//     print("Deposite:  $amount, New balance: $balance");
//   }

//   void withdraw(double amount) {
//     if (amount <= balance) {
//       balance -= amount;
//       print("Withdrew: $amount, New balance: $balance");
//     } else {
//       print("Insufficient Balance");
//     }
//   }

//   void showbalance() {
//     print("Account Balance is: $balance");
//   }
// }

// // saving account
// class SavingAcct extends BankAccount {
//   SavingAcct(
//       String accountNum, String holderName, double balance, String accountType)
//       : super(accountNum, holderName, balance, accountType);
// }

// // current account
// class CurrentAcct extends BankAccount {
//   CurrentAcct(
//       String accountNum, String holderName, double balance, String accountType)
//       : super(accountNum, holderName, balance, accountType);
// }

// void main() {
//   print("Enter Account Number: ");
//   String accountNum = stdin.readLineSync()!;
//   print("------------------------------------");
//   print("Enter Account Holder Name: ");
//   String holderName = stdin.readLineSync()!;
//   print("--------------------------------------");
//   print("Enter Initial balanace: ");
//   double initialBalance = double.parse(stdin.readLineSync()!);
//   print("Enter Account type: ");
//   String accountType = stdin.readLineSync()!;

//   // creating current account
//   CurrentAcct currentAct = CurrentAcct(
//     accountNum,
//     holderName,
//     initialBalance,
//     accountType
//   );

//   while (true) {
//     print("\n1. Deposite");
//     print("2. Withdraw");
//     print("3. Show balance");
//     print("4. Exit");

//     print("Enter Your choice: ");
//     int choice = int.parse(stdin.readLineSync()!);

//     switch (choice) {
//       case 1:
//         print("Enter amount to deposite: ");
//         double depositeAmt = double.parse(stdin.readLineSync()!);
//         currentAct.deposite(depositeAmt);
//         break;
//       case 2:
//         print("Enter amount to Withdraw: ");
//         double withdrawAmt = double.parse(stdin.readLineSync()!);
//         currentAct.withdraw(withdrawAmt);
//         break;
//       case 3:
//         currentAct.showbalance();
//       case 4:
//         exit(0);
//       default:
//         print("Invalide choice");
//     }
//   }
// }

abstract class BankAccount {
  String accountNum;
  String holderName;
  double balance;
  String accountType;

  BankAccount(this.accountNum, this.accountType, this.balance, this.holderName);

  void deposite(double amount) {
    balance += amount;
    print("Deposited $amount to $accountType, New balance: $balance");
  }

  void withdraw(double amount) {
    if (accountType == "Saving") {
      print("Can not withdraw from this account at the moment");
      return;
    }
    if (amount < balance) {
      print("Insufficient Balance in this account");
    } else {
      balance -= amount;
      print("Withdrew $amount from this $accountType, New Balance: $balance");
    }
  }

  void showBalance() {
    print("Your balance in $accountType with $accountNum is $balance");
  }
}

void main() {
  // smaple accounts for testing
  BankAccount savingAcct = BankAccount("AB123", "Andy", 100000, "Saving");
}
