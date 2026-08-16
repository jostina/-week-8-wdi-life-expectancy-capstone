import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="African Life Expectancy Predictor",
    page_icon="🌍",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "life_expectancy_model.joblib"
METADATA_PATH = BASE_DIR / "model_metadata.joblib"
IMPORTANCE_PATH = BASE_DIR / "feature_importance.csv"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_resource
def load_metadata():
    return joblib.load(METADATA_PATH)


@st.cache_data
def load_feature_importance():
    if IMPORTANCE_PATH.exists():
        return pd.read_csv(IMPORTANCE_PATH)

    return pd.DataFrame(
        columns=["Feature", "Importance"]
    )


# ============================================================
# LOAD FILES SAFELY
# ============================================================

try:
    model = load_model()
    metadata = load_metadata()
    feature_importance = load_feature_importance()

except FileNotFoundError:

    st.error(
        """
        Model files are missing.

        Please make sure the following files are in the same
        GitHub repository as app.py:

        • life_expectancy_model.joblib
        • model_metadata.joblib
        • feature_importance.csv
        """
    )

    st.stop()


# ============================================================
# PROJECT INFORMATION
# ============================================================

MODEL_NAME = metadata.get(
    "model_name",
    "Gradient Boosting Regressor"
)

FEATURES = metadata["features"]

DEFAULTS = metadata.get(
    "defaults",
    {}
)

FEATURE_LABELS = metadata.get(
    "feature_labels",
    {}
)


# ============================================================
# HEADER
# ============================================================

st.title("🌍 African Life Expectancy Predictor")

st.markdown(
    """
### Predicting Life Expectancy Using World Bank Development Indicators

This machine-learning application estimates life expectancy
using socioeconomic, health, education, infrastructure,
demographic, environmental and technology indicators from the
**World Bank World Development Indicators (WDI)** dataset.
"""
)

st.info(
    """
    **Capstone Project**

    54 African countries | 2000–2024 | World Bank WDI Dataset
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📊 Project Information")

    st.write("**Dataset:** World Bank WDI")

    st.write("**Countries:** 54 African countries")

    st.write("**Analysis period:** 2000–2024")

    st.write("**Target:** Life expectancy at birth")

    st.write(
        f"**Best model:** {MODEL_NAME}"
    )

    st.divider()

    st.header("🏆 Model Performance")

    st.metric(
        "MAE",
        "1.742 years"
    )

    st.metric(
        "RMSE",
        "2.280 years"
    )

    st.metric(
        "R²",
        "0.865"
    )

    st.divider()

    st.caption(
        "Developed as part of the AnalystLab Africa "
        "Data Science Internship — Week 8 Capstone."
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

st.header("🔮 Predict Life Expectancy")

st.write(
    """
    Enter the available development indicators below.
    The model will use these values to estimate life expectancy
    in years.
    """
)


# ============================================================
# INPUT FORM
# ============================================================

input_values = {}

# Use two columns to make the interface cleaner.
column_1, column_2 = st.columns(2)


for index, feature in enumerate(FEATURES):

    label = FEATURE_LABELS.get(
        feature,
        feature.replace("_", " ").title()
    )

    default_value = DEFAULTS.get(
        feature,
        0.0
    )

    # Handle missing defaults
    if pd.isna(default_value):
        default_value = 0.0

    default_value = float(default_value)


    # --------------------------------------------------------
    # Determine reasonable input ranges
    # --------------------------------------------------------

    if feature in [
        "electricity_access",
        "internet_usage",
        "literacy"
    ]:

        min_value = 0.0
        max_value = 100.0
        step = 0.1


    elif feature == "fertility":

        min_value = 0.0
        max_value = 15.0
        step = 0.1


    elif feature == "infant_mortality":

        min_value = 0.0
        max_value = 200.0
        step = 0.1


    elif feature == "unemployment":

        min_value = 0.0
        max_value = 100.0
        step = 0.1


    elif feature == "population_growth":

        min_value = -10.0
        max_value = 20.0
        step = 0.1


    elif feature == "gdp_growth":

        min_value = -50.0
        max_value = 50.0
        step = 0.1


    elif feature == "health_expenditure":

        min_value = 0.0
        max_value = 50.0
        step = 0.1


    elif feature == "physicians":

        min_value = 0.0
        max_value = 20.0
        step = 0.01


    elif feature == "co2_per_capita":

        min_value = 0.0
        max_value = 50.0
        step = 0.01


    elif feature == "gdp_per_capita":

        min_value = 0.0
        max_value = 100000.0
        step = 100.0


    elif feature == "log_gdp_per_capita":

        min_value = 0.0
        max_value = 20.0
        step = 0.01


    else:

        min_value = -100000.0
        max_value = 100000.0
        step = 0.1


    # Make sure default is inside allowed range
    default_value = max(
        min_value,
        min(default_value, max_value)
    )


    # --------------------------------------------------------
    # Display input
    # --------------------------------------------------------

    selected_column = (
        column_1
        if index % 2 == 0
        else column_2
    )

    with selected_column:

        input_values[feature] = st.number_input(
            label,
            min_value=float(min_value),
            max_value=float(max_value),
            value=float(default_value),
            step=float(step)
        )


# ============================================================
# GDP TRANSFORMATION
# ============================================================

# If GDP per capita is provided and the model expects
# log GDP per capita, calculate it automatically.

if (
    "gdp_per_capita" in input_values
    and "log_gdp_per_capita" in FEATURES
):

    input_values["log_gdp_per_capita"] = np.log1p(
        max(
            0,
            input_values["gdp_per_capita"]
        )
    )


# ============================================================
# CREATE MODEL INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame(
    [input_values],
    columns=FEATURES
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Life Expectancy",
    type="primary",
    use_container_width=True
)


if predict_button:

    try:

        prediction = model.predict(
            input_data
        )[0]

        prediction = float(prediction)


        # ----------------------------------------------------
        # Prediction Result
        # ----------------------------------------------------

        st.success(
            f"### Estimated Life Expectancy: {prediction:.1f} years"
        )


        # ----------------------------------------------------
        # Display result
        # ----------------------------------------------------

        result_col1, result_col2, result_col3 = st.columns(3)


        with result_col1:

            st.metric(
                "Predicted Life Expectancy",
                f"{prediction:.1f} years"
            )


        with result_col2:

            st.metric(
                "Model",
                "Gradient Boosting"
            )


        with result_col3:

            st.metric(
                "R²",
                "0.865"
            )


        st.info(
            """
            This prediction is generated from the development
            indicators entered above. It represents a model-based
            estimate and should not be interpreted as a causal
            prediction or medical advice.
            """
        )


    except Exception as error:

        st.error(
            f"Prediction error: {error}"
        )


# ============================================================
# MODEL PERFORMANCE SECTION
# ============================================================

st.divider()

st.header("📈 Model Performance")


performance_data = pd.DataFrame(
    {
        "Metric": [
            "MAE",
            "RMSE",
            "R²"
        ],

        "Value": [
            1.742,
            2.280,
            0.865
        ]
    }
)


performance_col1, performance_col2, performance_col3 = st.columns(3)


with performance_col1:

    st.metric(
        "Mean Absolute Error",
        "1.742 years"
    )

    st.caption(
        "Average prediction error."
    )


with performance_col2:

    st.metric(
        "Root Mean Squared Error",
        "2.280 years"
    )

    st.caption(
        "Penalizes larger prediction errors."
    )


with performance_col3:

    st.metric(
        "R² Score",
        "0.865"
    )

    st.caption(
        "86.5% of variation explained."
    )


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

st.divider()

st.header("🔍 Feature Importance")

st.write(
    """
    Feature importance shows which variables contributed most
    to the predictions made by the selected Gradient Boosting
    model.

    Important: feature importance indicates predictive
    contribution, not causation.
    """
)


if not feature_importance.empty:

    top_features = (
        feature_importance
        .sort_values(
            "Importance",
            ascending=False
        )
        .head(10)
        .copy()
    )

    top_features = top_features.set_index(
        "Feature"
    )

    st.bar_chart(
        top_features["Importance"]
    )


else:

    st.warning(
        "Feature-importance data is not available."
    )


# ============================================================
# ABOUT THE PROJECT
# ============================================================

st.divider()

st.header("📚 About This Project")

st.markdown(
    """
    ### Research Question

    **Can a country's life expectancy be predicted using
    development indicators from the World Bank World
    Development Indicators dataset?**

    ### Dataset

    The project uses the World Bank World Development
    Indicators dataset.

    The analysis focuses on:

    - 54 African countries
    - 2000–2024
    - Health indicators
    - Economic indicators
    - Education indicators
    - Infrastructure indicators
    - Demographic indicators
    - Environmental indicators
    - Technology indicators

    ### Machine Learning

    Three regression models were evaluated:

    1. Linear Regression
    2. Random Forest Regressor
    3. Gradient Boosting Regressor

    **Gradient Boosting achieved the best performance.**

    ### Final Results

    - MAE: **1.742 years**
    - RMSE: **2.280 years**
    - R²: **0.865**
    """
)


# ============================================================
# LIMITATIONS
# ============================================================

st.divider()

st.header("⚠️ Limitations")

st.markdown(
    """
    - The model identifies predictive relationships, not
      causal relationships.
    - World Bank indicators contain missing values.
    - Country-level development conditions differ substantially.
    - Model performance may vary for individual countries.
    - Predictions should be interpreted alongside expert
      knowledge and country-specific evidence.
    """
)


# ============================================================
# DATA SOURCE
# ============================================================

st.divider()

st.header("🌐 Data Source")

st.markdown(
    """
    **World Bank — World Development Indicators**

    https://datatopics.worldbank.org/world-development-indicators/
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AnalystLab Africa Data Science Internship — Week 8 Capstone | "
    "Jostina Ndavi | #AnalystLabAfrica"
)
