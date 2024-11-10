import 'package:flutter/material.dart';

class PasswordField extends StatefulWidget {
  final String labelText;
  final TextEditingController? controller;
  final FormFieldValidator<String>? validator;

  const PasswordField({
    super.key,
    required this.labelText,
    this.controller,
    this.validator,
  });

  @override
  PasswordFieldState createState() => PasswordFieldState();
}

class PasswordFieldState extends State<PasswordField> {
  bool _isPassVissible = false;

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      obscureText: !_isPassVissible,
      controller: widget.controller,
      validator: widget.validator,
      decoration: InputDecoration(
        labelText: widget.labelText,
        prefixIcon: const Icon(Icons.lock_outline),
        suffixIcon: IconButton(
          icon: Icon(
            _isPassVissible ? Icons.visibility : Icons.visibility_off,
          ),
          onPressed: () {
            setState(() {
              _isPassVissible = !_isPassVissible;
            });
          },
        ),
        border: const OutlineInputBorder(),
      ),
    );
  }
}
