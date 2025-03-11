 📧 Spam Detection Model 🚀  

 📌 Overview  
This project implements a **Spam Detection Model** using **Machine Learning (SVM)** to classify emails as **Spam (1) or Not Spam (0)**. It processes a dataset of email messages, cleans the text, extracts features, and trains a model to detect spam messages with high accuracy


## ⚙️ Features  
✅ **Preprocessing:** Removes special characters, stopwords, and URLs.  
✅ **Feature Extraction:** Converts text into numerical data using `CountVectorizer`.  
✅ **Machine Learning Model:** Uses **Support Vector Machine (SVM)** for classification.  
✅ **Accuracy:** Achieves **98%+ accuracy** in detecting spam messages.  
✅ **User Input Support:** Allows users to test custom email messages.  

---

## 🛠️ Tech Stack  
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn (`SVC` with linear kernel)  
- **Data Processing:** Pandas, NumPy  
- **Feature Extraction:** CountVectorizer  
- **Dataset:** SMS/Email Spam Dataset  

---

## 🚀 Installation & Usage  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/Gourav123125/Spam-detection-Model.git
cd Spam-detection-Model
```

### 2️⃣ **Install Dependencies**  
```sh
pip install pandas scikit-learn numpy
```

### 3️⃣ **Run the Model**  
```sh
python model.py
```

---

## 📊 Model Performance  
| Metric       | Score |
|-------------|-------|
| Accuracy    | 98.47% |
| Precision   | 1.00 (Spam) |
| Recall      | 0.89 (Spam) |
| F1-Score    | 0.94 (Spam) |

✅ **The model successfully detects spam with high precision.**  

---

## 📝 Example Usage  
### **Input:**  
> "Congratulations! You have won a free vacation. Click here to claim now."  
### **Output:**  
> **"Spam"** ✅  

---

## 🤝 Contributing  
Feel free to **fork this repository**, improve the model, and submit a **pull request**!  

---

## 📌 Author  
👤 **Gourav Bhatia**  
📧 Contact: [gouravbh786@gmail.com]  

---

## ⚖️ License  
This project is licensed under the **MIT License**.  

---

### ⭐ **If you found this project helpful, don't forget to give it a star!** ⭐

