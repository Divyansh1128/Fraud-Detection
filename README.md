# 🔍 Fraud Detection System

A real-time transaction analysis system that uses machine learning to detect potentially fraudulent transactions.

## 🌟 Features

- Real-time transaction analysis
- Interactive web interface
- RESTful API with Swagger documentation
- Transaction risk scoring
- Statistical insights

## 🚀 Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the server:
   ```bash
   npm run dev
   ```

3. Open http://localhost:3000 in your browser

## 🔧 API Endpoints

- POST `/api/detect` - Analyze a transaction
- GET `/api/stats` - Get system statistics

View complete API documentation at `/api-docs`

## 💡 Demo Scenario

Test the system with these scenarios:
- Low Risk: Amount < $500
- Medium Risk: Amount $500-$1000
- High Risk: Amount > $1000 or large transactions during night hours

## 🛠️ Tech Stack

- Node.js & Express
- Swagger UI for API documentation
- TailwindCSS for styling
- Real-time analysis engine