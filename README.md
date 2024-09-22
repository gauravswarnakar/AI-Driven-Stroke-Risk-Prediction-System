# AI-Driven-Stroke-Risk-Prediction-System

## Overview

This project aims to develop an AI-driven system to predict the risk of stroke in individuals based on various health parameters.

## HOW A STROKE HAPPENS:

- Ischemic Stroke: Caused by a blood clot that blocks or plugs a blood vessel in the brain.
- The clot may form in the brain’s blood vessels or travel from elsewhere in the body, like the heart.
- Hemorrhagic Stroke: Caused by a blood vessel that breaks and bleeds into the brain.
- This can happen due to high blood pressure or an aneurysm (weak spot) in a blood vessel.

### Understanding the Stroke Epidemic
Global Health Crisis: Stroke is the second leading cause of death worldwide, responsible for 11% of all deaths. WHO reports 15 million stroke cases annually, with 5 million deaths and 5 million permanent disabilities.
Challenges in Early Detection: Despite medical advancements, predicting stroke risk accurately is difficult due to the complex factors involved.
The Need for Innovation
Gaps in Current Approaches: Current tools rely on patient history and basic imaging, which may miss critical blood flow changes that indicate stroke risk.
Our Vision for Transformation: We aim to use advanced AI and medical imaging to provide accurate, non-invasive stroke risk assessments, moving from reactive to proactive stroke prevention

### Problem Statement

Inconsistent and Inaccurate Predictions: Traditional stroke risk assessments, like Doppler ultrasound or basic imaging, often fail due to patient variability and image quality. These methods struggle to detect subtle blood flow changes, leading to inconsistent and inaccurate predictions.
Reactive Healthcare System: The current system focuses on treating strokes after they occur rather than preventing them, leading to high death rates, severe disabilities, and long-term complications for survivors

### Our Solution

Integrating Advanced Medical Imaging with AIThe Unique Advantage
Personalized and Non-Invasive:
Provides a personalized stroke risk profile based on individual anatomy. The non-invasive method allows for continuous monitoring and early detection, reducing stroke likelihood and enabling timely intervention.
Early Detection, Better Outcomes:
Shifts focus from treatment to prevention, potentially lowering stroke incidence and reducing long-term care costs through timely intervention.
Scalability and Integration:
Designed to integrate with existing healthcare systems, making it scalable and adaptable to various settings, benefiting a wide range of patients.
Data Acquisition: We use CT, MRI, and ultrasound to capture high-resolution images of the carotid arteries, providing detailed views crucial for accurate modeling.
Geometric Modeling: We build a precise model of the carotid artery, incorporating local radius, curvature, and bifurcation points to understand blood flow dynamics.
Uncertainty Estimation: Our system addresses imaging limitations by quantifying uncertainties due to image resolution and anatomical variations, ensuring robust predictions.

### Features

- Data analysis and preprocessing
- Machine learning models for stroke risk prediction
- User-friendly interface for inputting health data
- Visualization of results and predictions

## Technologies Used
- Python
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Installation
To run this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/gauravswarnakar/AI-Driven-Stroke-Risk-Prediction-System.git
cd AI-Driven-Stroke-Risk-Prediction-System
pip install -r requirements.txt
