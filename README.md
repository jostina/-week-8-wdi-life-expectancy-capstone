# -week-8-wdi-life-expectancy-capstone
# 🌍 Predicting Life Expectancy in African Countries Using World Bank WDI



##  Live Demo

👉 https://african-life-expectancy.streamlit.app/

##  Project Overview

This project uses the World Bank World Development Indicators (WDI)
dataset to predict life expectancy across African countries using
machine learning.

The project covers **54 African countries** and the period
**2000–2024**.

The objective is to investigate whether socioeconomic, health,
education, infrastructure, demographic, environmental and technology
indicators can be used to predict life expectancy.

##  Research Question

> Can a country's life expectancy be predicted using development
> indicators from the World Bank World Development Indicators dataset?

##  Machine Learning

Three regression models were evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The **Gradient Boosting Regressor** achieved the best performance.

| Metric | Result |
|---|---:|
| MAE | 1.742 years |
| RMSE | 2.280 years |
| R² | 0.865 |

##  Dataset

The project uses the World Bank World Development Indicators dataset.

**Source:**  
https://datatopics.worldbank.org/world-development-indicators/

The analysis focuses on:

- 54 African countries
- 2000–2024
- Life expectancy as the target variable
- Economic indicators
- Health indicators
- Education indicators
- Infrastructure indicators
- Demographic indicators
- Environmental indicators
- Technology indicators

##  Deployment

The machine-learning model was deployed using **Streamlit**.

👉 **Live application:**  
https://african-life-expectancy.streamlit.app/

## ⚠️ Limitations

This model identifies predictive relationships rather than causal
relationships. Feature importance should therefore not be interpreted
as proof that changing a particular indicator will directly cause
life expectancy to change.

The application is intended for educational and analytical purposes.

## 👩🏽‍💻 Author

**Jostina Ndavi**

Data Science / Machine Learning

**AnalystLab Africa Data Science Internship — Week 8 Capstone**

#AnalystLabAfrica
