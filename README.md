# Password_checker
A Python-based cybersecurity tool that analyzes password strength using regular expressions (regex), providing a dynamic score and real-time security feedback.

Password Strength Checker

A lightweight, local Python tool designed to assess the strength of passwords based on standard security criteria. This project evaluates passwords dynamically and provides actionable cryptographic feedback to help users generate more robust credentials.

🚀 Features
Multi-Criteria Analysis: Checks input against five distinct security baselines (length, uppercase, lowercase, numbers, and special characters).
Dynamic Scoring: Computes an immediate security score from $0$ to $5$.
Actionable Feedback: Generates precise recommendations detailing exactly what character types are missing.
Console-Based Interface: Runs seamlessly within any standard terminal or IDE like VS Code.

📊 Evaluation Criteria
The program tracks five specific criteria using Python's regular expressions (re) module:

Metric,              Requirement
Length,              ≥8 characters
Uppercase,           At least one character (A−Z)
Lowercase,           At least one character (a−z)
Numbers,             At least one digit (0−9)
Special Characters,  At least one symbol (e.g., !, @, #, $, %)

## 🛠️ How to Run
1. Download `password_checker.py`.
2. Open your terminal or VS Code terminal and run:
```bash
   python password_checker.py
