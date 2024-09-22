document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Extract values from the form
    const age = document.getElementById('age').value;
    const bloodPressure = document.getElementById('bloodPressure').value;
    const cholesterol = document.getElementById('cholesterol').value;
    const strokeHistory = document.getElementById('strokeHistory').value;
    const smokingStatus = document.getElementById('smokingStatus').value;
    const diabetesStatus = document.getElementById('diabetesStatus').value;

    // Here you would send a request to your backend to get the prediction
    // For example:
    // fetch('/predict', {
    //     method: 'POST',
    //     body: JSON.stringify({ age, bloodPressure, cholesterol, strokeHistory, smokingStatus, diabetesStatus }),
    //     headers: { 'Content-Type': 'application/json' }
    // })
    // .then(response => response.json())
    // .then(data => {
    //     document.getElementById('result').innerText = `Risk Prediction: ${data.risk}`;
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    // });

    // For now, just displaying a mock result
    document.getElementById('result').innerText = "Risk Prediction: High Risk (Mock Result)";
});
