import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load and clean the dataset
df = pd.read_csv("C:/Users/hp/Downloads/spam.csv", encoding="latin1")

# Rename relevant columns
df = df.iloc[:, :2]  # Keep only the first two columns
df.columns = ["label", "message"]

# Convert labels to binary (spam=1, ham=0)
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Drop any missing values
df.dropna(inplace=True)

# Text Cleaning Function
def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
    text = re.sub(r"[^a-zA-Z]", " ", text)  # Keep only letters
    text = text.lower().strip()  # Convert to lowercase and remove spaces
    return text

# Apply text cleaning
df["cleaned_text"] = df["message"].apply(clean_text)

# Convert text to numerical data
vectorizer = CountVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(df["cleaned_text"]).toarray()
y = df["label"].values  # Labels (1 = spam, 0 = not spam)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train SVM Model
model = SVC(kernel="linear")
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Function to predict spam
def predict_spam(email):
    email = clean_text(email)
    vectorized_email = vectorizer.transform([email]).toarray()
    return "Spam" if model.predict(vectorized_email)[0] == 1 else "Not Spam"

# Example usage
print(predict_spam("Congratulations! You have won a free vacation. Click here to claim now."))
