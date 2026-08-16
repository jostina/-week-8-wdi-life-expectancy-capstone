# Predicting Life Expectancy in African Countries Using World Bank Development Indicators

## 1. Introduction
Life expectancy is an important population-health and development indicator. It reflects the combined influence of health systems, socioeconomic conditions, education, infrastructure, demographic patterns and environmental factors. This project uses World Bank World Development Indicators to investigate whether these development measures can be used to predict life expectancy across African countries.

## 2. Problem Statement
**Can a country's life expectancy be predicted using socioeconomic, health, education, infrastructure, demographic, environmental and technology indicators from the World Bank WDI dataset?**

## 3. Objectives
- Prepare WDI data for analysis.
- Explore development and life-expectancy patterns.
- Build and compare regression models.
- Evaluate predictive performance.
- Identify useful predictive variables.
- Deploy the final model using Streamlit.

## 4. Dataset
The WDI source contains indicators for countries and economies over multiple decades. This project focuses on **54 African countries** and **2000–2024**. The target is `SP.DYN.LE00.IN`, Life expectancy at birth, total (years).

## 5. Methodology
The data was filtered to African countries and reshaped from WDI's indicator/year structure into country-year observations. Relevant economic, health, education, infrastructure, demographic, environmental and technology indicators were selected. Missing predictors were handled using median imputation within the ML preprocessing pipeline. GDP per capita was log-transformed because of skewness.

A time-based evaluation strategy was used: **2000–2019 for training** and **2020–2024 for testing**. Three regression algorithms were compared: Linear Regression, Random Forest Regressor and Gradient Boosting Regressor.

## 6. EDA Findings
The notebook contains the distribution of life expectancy, its trend over time, country comparisons, development-indicator scatter plots and correlation analysis. Insert the exact observations from your executed notebook here rather than using generic claims.

## 7. Model Development and Evaluation
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| **Gradient Boosting** | **1.742** | **2.280** | **0.865** |

Gradient Boosting was the best-performing model. MAE of 1.742 years means predictions differed from observed life expectancy by about 1.74 years on average. R² of 0.865 means the model explained approximately 86.5% of variation in the holdout evaluation data.

## 8. Insights
The results show that the selected development indicators collectively contain substantial predictive information about life expectancy. The strongest feature-importance findings should be inserted from the notebook's actual `feature_importance` output. Feature importance indicates predictive contribution and should not be interpreted as proof of causal relationships.

## 9. Recommendations
1. Use multiple development indicators together when assessing population-health outcomes.
2. Improve the completeness, quality and timeliness of national development statistics.
3. Use predictive models as decision-support tools rather than replacements for policy expertise.
4. Investigate important predictors with causal and country-specific methods before implementing interventions.

## 10. Deployment
The final model is prepared for Streamlit deployment. The application provides an interface for entering development indicators and returning a model-based life-expectancy estimate, together with model performance information.

## 11. Limitations
This model is predictive rather than causal. WDI has substantial missingness across indicators, and the project therefore uses a selected feature set. A time-based holdout improves realism but does not eliminate all dependence among country-year observations.

## 12. Conclusion
This capstone demonstrates an end-to-end data science workflow using real World Bank development data. Gradient Boosting achieved an MAE of **1.742 years**, RMSE of **2.280 years**, and R² of **0.865** on the holdout evaluation period. The project shows how machine learning can support exploration of development and population-health patterns while emphasizing the need for careful interpretation and further causal analysis.

## 13. Data Source
World Bank World Development Indicators: https://datatopics.worldbank.org/world-development-indicators/
