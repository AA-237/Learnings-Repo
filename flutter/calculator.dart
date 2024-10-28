import 'dart:io';

class Calculator {
  double add(double a, double b) => a + b;
  double substract(double a, double b) => a - b;
  double divide(double a, double b) {
    if (b == 0) {
      print("Dividing by zero is not allowed");
      return double.nan;
    }
    return a / b;
  }

  double multiply(double a, double b) => a * b;
  double module(double a, double b) => a % b;
}

void main() {
  print("I love coding .................... bla bla");

  var calc = Calculator();
  bool startCal = true;

  while (startCal) {
    print("\n Select an option");
    print("1. Addition");
    print("2. Subtraction");
    print("3. Multiplication");
    print("4. Division");
    print("5. Module");
    print("6. Exit");

    stdout.write("Enter your choice (1-6): ");
    // int choice = int.parse(stdin.readLineSync()!);
    int choice = 2;

    if (choice == 6) {
      print("Thanks for using the app");
      startCal = false;
      break;
    }

    stdout.write("Enter thew first number: ");
    double num1 = double.parse(stdin.readLineSync()!);

    stdout.write("Enter the second number: ");
    double num2 = double.parse(stdin.readLineSync()!);

    double result;

    switch (choice) {
      case 1:
        result = calc.add(num1, num2);
        print(result);
        break;
      case 2:
        result = calc.substract(num1, num2);
        print(result);
      case 3:
        result = calc.multiply(num1, num2);
        print(result);
      case 4:
        result = calc.divide(num1, num2);
        print(result);
      case 5:
        result = calc.module(num1, num2);
        print(result);
      default:
        print("Invalide operation, please select a valid option");
    }
  }
}
