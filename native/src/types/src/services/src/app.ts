// src/app.ts
import { FileService } from './services/FileService';
import express from 'express';
import path from 'path';

const app = express();
const fileService = new FileService();

app.use(express.json());

app.post('/api/process-file', async (req, res) => {
    try {
        const { filePath } = req.body;
        const processedBuffer = await fileService.processFile(filePath);
        res.send(processedBuffer);
    } catch (error) {
        res.status(500).json({ error: 'Failed to process file' });
    }
});

app.post('/api/analyze-text', async (req, res) => {
    try {
        const { text } = req.body;
        const analysis = await fileService.analyzeText(text);
        res.json(analysis);
    } catch (error) {
        res.status(500).json({ error: 'Failed to analyze text' });
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
