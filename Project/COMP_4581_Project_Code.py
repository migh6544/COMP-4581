##
# Michael Ghattas & Mike Worden
# COMP 4581 - Project
# Mar/8/2025
##



import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import trange  # Standard progress tracking
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.exceptions import NotFittedError
from sklearn.metrics import median_absolute_error
import matplotlib.pyplot as plt


class ConformalCoverForest:
    """
    Conformal Prediction using Random Forest for classification-based uncertainty estimation.
    This version improves residual estimation to prevent overfitting and enhances generalization.

    Attributes:
    - alpha: Significance level (1 - confidence level).
    - base_model: The base regression model (default is RandomForestRegressor).
    - residuals: Stores the absolute residuals from calibration.
    - train_time: Tracks model training time.
    - predict_time: Tracks prediction interval computation time.
    - label_encoder: Encodes categorical target labels.
    """

    def __init__(self, alpha=0.05, base_model=None):
        """
        Initializes the Conformal Cover Forest model with a specified confidence level.

        Parameters:
        - alpha (float): Significance level (e.g., 0.05 means 95% confidence).
        - base_model: The base regression model (default: RandomForestRegressor with better hyperparameters).
        """
        self.alpha = alpha
        self.base_model = base_model if base_model else RandomForestRegressor(
            n_estimators=300, max_depth=10, bootstrap=True, random_state=42
        )
        self.residuals = None
        self.train_time = 0.0
        self.predict_time = 0.0
        self.is_fitted = False  # Track if model is fitted
        self.label_encoder = None  # For encoding categorical target labels


    def preprocess_data(self, X, y):
        """
        Converts categorical features and target labels into numeric format.

        Parameters:
        - X (DataFrame or array-like): Feature matrix (may contain categorical columns).
        - y (Series or array-like): Target labels (categorical or numerical).

        Returns:
        - X_processed: Numeric feature matrix.
        - y_processed: Encoded numeric target variable.
        """

        X = pd.DataFrame(X)  # Ensure X is a DataFrame

        # Convert categorical features to numerical (One-Hot Encoding)
        for col in X.select_dtypes(include=['object']).columns:
            one_hot = pd.get_dummies(X[col], prefix=col)
            X = X.drop(col, axis=1)
            X = pd.concat([X, one_hot], axis=1)

        # Encode target labels if they are categorical
        if isinstance(y, pd.Series) and y.dtype == 'object':
            self.label_encoder = LabelEncoder()
            y = self.label_encoder.fit_transform(y)

        return X.values, y


    def fit(self, X, y):
        """
        Trains the model on provided data and calculates residuals for conformal prediction.

        Parameters:
        - X (array-like): Feature matrix.
        - y (array-like): Target variable (discrete class labels).

        Steps:
        1. Preprocesses categorical data into numeric format.
        2. Splits data into training (80%) and calibration (20%) sets.
        3. Fits the RandomForest model on the training set.
        4. Predicts on the calibration set and computes residuals using MAD + noise.
        """

        X, y = self.preprocess_data(X, y)  # Convert categorical data

        # Increase calibration set size for better generalization (80-20 split)
        X_train, X_calib, y_train, y_calib = train_test_split(X, y, test_size=0.2, random_state=42)

        print("Training model...")
        start_time = time.time()
        for _ in trange(1, desc="Training Progress"):
            self.base_model.fit(X_train, y_train)
        self.train_time = time.time() - start_time
        self.is_fitted = True

        print("Computing residuals on calibration set...")
        y_pred_calib = self.base_model.predict(X_calib)

        # Compute residuals using Median Absolute Deviation (MAD) and Gaussian noise
        self.residuals = np.abs(y_calib - y_pred_calib)
        mad = median_absolute_error(y_calib, y_pred_calib)

        # FIX: Reduce excess variability by scaling noise contribution
        self.residuals += mad + np.random.normal(0, mad * 0.5, size=self.residuals.shape)


    def predict(self, X_test):
        """
        Generates conformal prediction intervals.

        Parameters:
        - X_test (array-like): Feature matrix for predictions.

        Returns:
        - lower_bounds: Lower bound predictions.
        - upper_bounds: Upper bound predictions.
        """
        
        if not self.is_fitted:
            raise NotFittedError("Model must be fitted before predicting. Call `fit()` first.")

        print("Generating predictions...")
        X_test, _ = self.preprocess_data(X_test, np.zeros(len(X_test)))  # Encode test features

        start_time = time.time()
        y_pred = self.base_model.predict(X_test)
        q_alpha = np.quantile(self.residuals, 1 - self.alpha)

        lower_bounds = np.floor(y_pred - q_alpha)  # Rounded to discrete labels
        upper_bounds = np.ceil(y_pred + q_alpha)
        self.predict_time = time.time() - start_time

        return lower_bounds, upper_bounds


# --- Generate Synthetic Data ---
np.random.seed(42)
subjects = ["Health", "Entertainment", "Sports", "Politics", "Technology"]
num_samples = 100

data = pd.DataFrame({
    "Subject": np.random.choice(subjects, num_samples),
    "Feature1": np.random.randn(num_samples) * 100 + 500,
    "Feature2": np.random.randn(num_samples) * 50 + 200,
    "Actual_Count": np.random.randint(3900, 4100, num_samples)
})

# --- Train Model ---
X = data.drop(columns=["Actual_Count", "Subject"])
y = data["Actual_Count"]
model = ConformalCoverForest(alpha=0.05)
model.fit(X, y)

# --- Predict and Evaluate ---
X_test = X[:10]
lower, upper = model.predict(X_test)

# --- Save Output CSV ---
output_df = pd.DataFrame({
    "Subject": data["Subject"][:10],
    "Actual_Count": y[:10],
    "Lower_Bound": lower,
    "Upper_Bound": upper,
    "Within": ((y[:10] >= lower) & (y[:10] <= upper)).astype(int)  # One-hot encoding for correctness
})
output_csv = "COMP_4581_Project_Output.csv"
output_df.to_csv(output_csv, index=False)
print(f"Output saved to {output_csv}")

# --- Save Log File ---
log_file = "COMP_4581_Project_Log.txt"
with open(log_file, "w") as log:
    log.write(f"Model Execution Summary:\n")
    log.write(f"Training Time: {model.train_time:.4f} seconds\n")
    log.write(f"Prediction Time: {model.predict_time:.4f} seconds\n")
    log.write(f"Total Run Time: {model.train_time + model.predict_time:.4f} seconds\n")

print(f"Log saved to {log_file}")

# --- Generate and Save Plot, Aggregate Data, and Ensure One Entry Per Category ---
output_df_grouped = output_df.groupby("Subject", as_index=False).mean()

plt.figure(figsize=(12, 6))
categories = output_df_grouped["Subject"]
actual_counts = output_df_grouped["Actual_Count"]
lower_bounds = output_df_grouped["Lower_Bound"]
upper_bounds = output_df_grouped["Upper_Bound"]

# Compute error bar range
error_bars = [actual_counts - lower_bounds, upper_bounds - actual_counts]

# Scatter plot for actual counts
plt.scatter(categories, actual_counts, color="black", label="Actual Count", zorder=3)

# Error bars for prediction intervals
plt.errorbar(categories, actual_counts, yerr=error_bars, fmt="o", color="blue", label="Prediction Interval")

plt.xlabel("News Subject")
plt.ylabel("Article Count")
plt.title("Conformal Prediction Intervals for News Subjects")

# Move legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout and save
plt.tight_layout()
plt.savefig("COMP_4581_Project_Plot.png", bbox_inches="tight", dpi=300)

print("Plot saved as COMP_4581_Project_Plot.png")



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##