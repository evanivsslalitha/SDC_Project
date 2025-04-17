
# **SDC_Project**  
### *AWS Lambda Layers for Code Reusability*

---

## 📌 Overview  
This project demonstrates **code reusability in AWS Lambda** by using **Lambda Layers**. The core idea is to modularize commonly used functions—such as account number validation—into a shared layer, enabling cleaner, more maintainable code across multiple Lambda functions.

---

## ⚙️ Functionality  
Each Lambda function simulates an aspect of an account management system:

- **`account_validation.py`**: Validates if an account number is exactly 10 digits.  
- **`createaccount.py`**: Creates a new account if validation passes.  
- **`getaccountbalance.py`**: Retrieves the current balance for a valid account.  
- **`updateaccountbalance.py`**: Updates the account balance for a valid account.  

---

## 🔁 Reusability with Lambda Layers  
The `account_validation.py` file is used as a **Lambda Layer**, which is imported into each function using:

```python
import account_validation as validationlayer
```

This approach ensures **DRY (Don't Repeat Yourself)** principles by keeping common logic centralized.

---

## 🧪 Sample Event Input  

```json
{
  "AcctNo": "1234567890",
  "Amount": 500
}
```

---

## 🧰 Technologies Used  
- 🟢 Python  
- ☁️ AWS Lambda  
- 📦 AWS Lambda Layers  
- 📁 GitHub  

---

## 🚀 How to Use  

1. Upload `account_validation.py` as a **Lambda Layer**.  
2. Create individual Lambda functions for:
   - `createaccount`
   - `getaccountbalance`
   - `updateaccountbalance`
3. Attach the Lambda Layer to each function.  
4. Deploy and test each Lambda function with relevant event inputs.

---

## 📄 Report  
Refer to `A2_221003072.pdf` for the detailed project report.

---

## 🙋‍♀️ Author  

**evanivsslalitha**  
_B.Tech CSE | AI & ML | Cloud-Based AIML Speciality_
