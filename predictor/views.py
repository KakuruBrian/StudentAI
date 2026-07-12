from django.shortcuts import render
import joblib
import pandas as pd
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained pipeline
MODEL_PATH = BASE_DIR / "model" / "student_pipeline.pkl"
model = joblib.load(MODEL_PATH)

# Debug: Print the features expected by the model
print("=" * 60)
print("MODEL LOADED FROM:", MODEL_PATH)
print("Expected Features:")
#print(model.feature_names_in_)
print("=" * 60)


def home(request):
    return render(request, "home.html")


def predict(request):

    if request.method == "POST":

        try:
            student = pd.DataFrame({
                "sex": [request.POST.get("sex")],
                "age": [int(request.POST.get("age"))],
                "studytime": [int(request.POST.get("studytime"))],
                "failures": [int(request.POST.get("failures"))],
                "absences": [int(request.POST.get("absences"))],
                "G1": [int(request.POST.get("G1"))],
                "G2": [int(request.POST.get("G2"))],
                "higher": [request.POST.get("higher")],
            })

            # Debug: Show the submitted data
            print("\nSubmitted Student Data:")
            #print(student)

            prediction = model.predict(student)[0]

            probability = model.predict_proba(student)[0]

            confidence = round(max(probability) * 100, 2)

            if prediction == 1:
                result = "PASS ✅"
                advice = (
                    "Keep attending classes regularly, maintain your study "
                    "routine, and continue aiming for higher education."
                )
            else:
                result = "FAIL ❌"
                advice = (
                    "Increase study time, reduce absences, seek academic support, "
                    "and improve continuous assessment performance."
                )

            context = {
    "prediction": result,
    "confidence": confidence,
    "confidence_angle": round((confidence / 100) * 360),
    "advice": advice,
}

            return render(request, "result.html", context)

        except Exception as e:
            print("\nERROR:")
            #print(e)

            return render(request, "predict.html", {
                "error": str(e)
            })
        

    return render(request, "predict.html")

def about(request):
    return render(request, "about.html")