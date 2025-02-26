// src/types/native.d.ts
declare module 'native-processor' {
    export class FileProcessor {
        processBuffer(buffer: Buffer): Buffer;
        analyze(text: string): {
            wordCount: number;
            length: number;
        };
    }
}
