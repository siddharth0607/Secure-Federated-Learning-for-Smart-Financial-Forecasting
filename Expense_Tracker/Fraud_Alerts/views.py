import os
import json
import pickle
import numpy as np
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Required for AJAX POST

# Load the Fraud Detection Model
MODEL_PATH = os.path.join(settings.BASE_DIR, "Fraud_Alerts/models/fraud_detection_model.pkl")

with open(MODEL_PATH, "rb") as model_file:
    fraud_model = pickle.load(model_file)

@login_required
def fraud_alerts_view(request):
    """Render the fraud alerts page."""
    return render(request, "Fraud_Alerts/fraud_index.html")

@csrf_exempt  # Exempt CSRF for AJAX requests
def predict_fraud(request):
    """Predict if a transaction is fraudulent using the ML model."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Read JSON data

            # Extract inputs
            amount = float(data.get("amount", 0))
            category = data.get("category", "")

            # Ensure valid input
            if amount <= 0:
                return JsonResponse({"error": "Invalid transaction amount."}, status=400)

            # Prepare data for model (modify if more features are needed)
            input_data = np.array([[amount]])  # Adjust input features based on your model

            # Get model prediction (0 = Legit, 1 = Fraudulent)
            prediction = fraud_model.predict(input_data)[0]
            result = "Fraudulent" if prediction == 1 else "Legit"

            return JsonResponse({"result": result})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except ValueError:
            return JsonResponse({"error": "Invalid data type."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)
