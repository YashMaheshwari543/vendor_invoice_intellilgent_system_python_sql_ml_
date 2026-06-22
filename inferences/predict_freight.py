import joblib
import pandas as pd

from pathlib import Path

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "Freight_csot_prediction"
    / "models"
    / "predict_freight_model.pkl"
)

def load_model(model_path = MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_freight_cost(input_data):
    """
    Predict freight cost for new vendor invoices.
    
    Parameters
    ----------
    input_data : dict
    
    Returns
    -------
    pd.DataFrame with predicted freight cost
    """
    
    model = load_model()
    input_df = pd.DataFrame({
        "Dollars": [input_data["Dollars"]]
    })
    
    # Generate predictions and round them for a clean dollar amount
    prediction = model.predict(input_df)[0].round()
    
    return {
    "Predicted_Freight": prediction
}

if __name__ == "__main__":
    
    # Example inference run (local testing)
    sample_data = {
        "Dollars": [18500, 5000, 300, 200]
    }
    
    prediction = predict_freight_cost(sample_data)
    print(prediction)