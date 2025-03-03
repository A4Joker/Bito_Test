// processor.ts
import { calculate } from './build/Release/calculator';

export class NumberProcessor {
    processValue(input: number): number {
        // This line depends on the C++ multiplier value
        const result = calculate(input);  // Will be impacted if C++ multiplier changes
        return result;
    }

    displayResult(value: number): string {
        const processed = this.processValue(value);
        // This message assumes the C++ multiplier is 2
        return `Value doubled: ${processed}`;  // Will be incorrect if C++ multiplier changes
    }
}
