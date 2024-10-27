export async function detectFraud(transaction) {
  const { amount, time } = transaction;
  
  // Demo threshold-based detection
  const isSuspicious = amount > 1000 || 
    (amount > 500 && time >= 0 && time <= 6);
  
  return {
    transactionId: Date.now(),
    timestamp: new Date().toISOString(),
    risk: isSuspicious ? 'HIGH' : 'LOW',
    score: isSuspicious ? 0.8 : 0.2,
    prediction: isSuspicious ? 'Potentially Fraudulent' : 'Likely Legitimate',
    features: {
      amount,
      time,
      riskFactors: isSuspicious ? ['Large amount', 'Suspicious timing'] : []
    }
  };
}