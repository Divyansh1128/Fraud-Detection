import express from 'express';
import { detectFraud } from '../services/fraudDetection.js';

export const router = express.Router();

router.post('/detect', async (req, res) => {
  try {
    const { amount, time } = req.body;
    const result = await detectFraud({ amount, time });
    res.json(result);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

router.get('/stats', (req, res) => {
  res.json({
    totalTransactions: 1000,
    fraudulentTransactions: 50,
    accuracy: 0.95,
    lastUpdated: new Date().toISOString()
  });
});