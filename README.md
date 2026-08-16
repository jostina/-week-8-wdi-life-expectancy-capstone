# -week-8-wdi-life-expectancy-capstone
Predicting Life Expectancy in African Countries Using World Bank WDI

AnalystLab Africa Data Science Internship — Week 8 Capstone

Project overview

This project investigates whether socioeconomic, health, education, infrastructure, demographic, environmental and technology indicators from the World Bank World Development Indicators (WDI) can be used to predict life expectancy across African countries.

Research question: Can a country's life expectancy be predicted using World Bank development indicators?

Dataset

Source: World Bank World Development Indicators (WDI): https://datatopics.worldbank.org/world-development-indicators/

The project focuses on 54 African countries and 2000–2024. The target is Life expectancy at birth, total (years) (SP.DYN.LE00.IN).

Methodology

Load and inspect WDI data.

Filter to African countries.

Select relevant development indicators.

Reshape the WDI data into country-year observations.

Handle missing predictor values using median imputation in the modeling pipeline.

Apply log transformation to GDP per capita.

Perform EDA and correlation analysis.

Train models using 2000–2019.

Evaluate on 2020–2024.

Compare Linear Regression, Random Forest and Gradient Boosting.

Deploy the best model with Streamlit.

Model performance

Model

MAE

RMSE

R²

Gradient Boosting

1.742

2.280

0.865

Gradient Boosting was the best-performing model. MAE of 1.742 years means predictions were about 1.74 years away from observed life expectancy on average. R² of 0.865 means approximately 86.5% of the variation in the holdout data was explained by the model.

Deployment

Run locally:

pip install -r requirements.txt
streamlit run app.py

Required model artifacts:

life_expectancy_model.joblib

model_metadata.joblib

Repository structure

wdi-life-expectancy-capstone/
├── app.py
├── life_expectancy_model.joblib
├── model_metadata.joblib
├── feature_importance.csv
├── model_comparison.csv
├── requirements.txt
├── WDI_Life_Expectancy_Capstone.ipynb
├── README.md
└── charts/

Limitations

This is a predictive model, not a causal model. Feature importance does not prove that changing an indicator will cause life expectancy to change. WDI also contains substantial missingness across indicators, so the project uses a selected subset.

Author

Jostina Ndavi

AnalystLab Africa Data Science Internship — Week 8 Capstone

#AnalystLabAfrica
