// src/services/FileService.ts
import { FileProcessor } from 'native-processor';
import fs from 'fs/promises';

export class FileService {
    private processor: FileProcessor;

    constructor() {
        this.processor = new FileProcessor();
    }

    async processFile(filePath: string): Promise<Buffer> {
        try {
            const fileBuffer = await fs.readFile(filePath);
            const processedBuffer = this.processor.processBuffer(fileBuffer);
            return processedBuffer;
        } catch (error) {
            console.error('Error processing file:', error);
            throw error;
        }
    }

    async analyzeText(text: string): Promise<{
        wordCount: number;
        length: number;
        averageWordLength: number;
    }> {
        try {
            const analysis = this.processor.analyze(text);
            return {
                ...analysis,
                averageWordLength: analysis.length / analysis.wordCount
            };
        } catch (error) {
            console.error('Error analyzing text:', error);
            throw error;
        }
    }
}
