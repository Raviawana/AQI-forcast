# Conclusion — AQI Forecasting Study

## Summary of results
- For **Stage 1 (AQI(t) — nowcast)** the best-performing ML model was **RandomForest** with RMSE = **0.059** (MAE/R2 available in metrics file).
- For **Stage 2 (AQI(t+1) — one-step-ahead forecast)** the best-performing ML model was **RandomForest** with RMSE = **0.059**.
- Among the deep-learning models, the best was **LSTM** with RMSE = **4.937**.

## Interpretation

The best ML model (RandomForest) improves RMSE by ~98.814% over the best deep model (LSTM).

Overall, results indicate that:
- The forecasting task for **t+1** is inherently more challenging than nowcasting **t**; model performance (RMSE/MAE) is typically worse for t+1 than for t, but this depends on the series volatility.
- Simpler ML models (e.g., RandomForest, Linear models) can be competitive for short-horizon AQI forecasts, especially when robust lag & rolling features are used.
- Deep models (LSTM/CNN/Transformer) can capture sequential dynamics and may outperform ML models if sufficient training data and hyperparameter tuning are available, otherwise they might overfit or underperform on small datasets.

## Limitations
- The reported performance depends on data quality, missing-value handling, window size, and feature engineering choices.
- Single-split train/test evaluation gives a quick comparison but a walk-forward evaluation (rolling-origin) would provide a more robust assessment.
- No exogenous variables (weather, emissions, traffic) were included in the univariate baseline; including them could improve forecasts.

## Recommendations and future work
- Perform walk-forward validation and nested hyperparameter tuning for more robust estimates.
- Experiment with hybrid models (ML features + LSTM) and ensemble stacking.
- Try multi-step and probabilistic forecasting to quantify uncertainty (prediction intervals).

## Final answer to research question
- Based on the experiments, the best model for 1-step-ahead AQI forecasting achieved an RMSE of **0.059** (model: **RandomForest**) which indicates [insert domain-meaningful error interpretation here].

## Appendix — saved artifacts
- ML metrics: /Users/ravigurjar/Desktop/temp/sample/dessertation/asset/forcast/ml
- Deep metrics & models: /Users/ravigurjar/Desktop/temp/sample/dessertation/asset/forcast/deep