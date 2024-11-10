import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
  final String labelText;
  final IconData icon;
  final TextInputType keyboardType;
  final FormFieldValidator<String>? validator;
  final TextEditingController? controller;

  const CustomTextField({
    super.key,
    required this.labelText,
    required this.icon,
    this.keyboardType = TextInputType.text,
    this.validator,
    this.controller,
  });

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      keyboardType: keyboardType,
      decoration: InputDecoration(
        labelText: labelText,
        prefixIcon: Icon(icon),
        border: const OutlineInputBorder(),
      ),
      validator: validator,
    );
  }
}
