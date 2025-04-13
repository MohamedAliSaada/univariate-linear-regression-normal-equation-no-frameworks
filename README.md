# 🔍 Univariate Linear Regression with Bias Term

This project demonstrates a simple **univariate linear regression** using Python, NumPy, and Pandas. The model predicts a continuous target variable (`el_power`) based on a single input feature (`time`) using the **normal equation**. A bias term (intercept) is included in the regression model to improve prediction accuracy.

---

## 📁 Project Structure

```
linear-regression-model/
│
├── linear_regression.py       # Main Python script (regression model)
├── ex_1.csv                   # Input dataset
├── model.png                  # Visual explanation of bias term
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation (this file)
```

---

## 📊 Dataset: `ex_1.csv`

The dataset contains two columns:

- `time`: A continuous feature (e.g., timestamp or sequential time unit)
- `el_power`: The target variable (e.g., electricity consumption or output)

All data is **normalized** (zero mean and unit variance) before fitting the model.

---

## ⚙️ How the Model Works

The linear regression equation with bias term is:

```
y = b + w * x
```

Or in matrix form using the **normal equation**:

```
w = (Xᵀ X)^(-1) Xᵀ y
```

Where:
- `X` is the feature matrix with a bias column
- `y` is the target vector
- `w` includes both bias and weight

---

## 📌 Key Features

- Automatic normalization of input features
- Adds a bias term to improve prediction performance
- Uses the closed-form solution (Normal Equation)
- Visualizes predicted vs actual data using `matplotlib`

---

## 🛠️ Setup Instructions

1. Clone this repo or download the ZIP.
2. Make sure `ex_1.csv` is in the same directory.
3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the model:

```bash
python linear_regression.py
```

---

## 📈 Output

- Prints the final regression equation:
  ```
  Model: y = [weight] * x + [bias]
  ```
- Displays a scatter plot of actual data and a line plot of predicted values.

---

## 🧠 Bias Term Explanation

A **bias term** (also called intercept) allows the regression line to **shift vertically**, improving model flexibility. Without it, the line is forced to pass through the origin, which may not reflect the true relationship in the data.

![Model Explanation](model.png)

---

## 📦 Dependencies

- `numpy`
- `pandas`
- `matplotlib`

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Feel free to fork this repository, improve the model (e.g., support multiple features), or add regularization and raise a pull request!

---

## 📄 License

This project is licensed under the MIT License.

---

## ✉️ Contact

For questions or feedback, feel free to open an issue or reach out!
