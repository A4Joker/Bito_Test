// calculator.cpp
#include <napi.h>

Napi::Value Calculate(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();
    
    // This line is critical - if changed, TypeScript code will be impacted
    int multiplier = 2;  // If this value changes, it affects the TypeScript result
    
    if (!info[0].IsNumber()) {
        throw Napi::Error::New(env, "Expected number as argument");
    }

    double input = info[0].As<Napi::Number>().DoubleValue();
    double result = input * multiplier;  // TypeScript depends on this calculation
    
    return Napi::Number::New(env, result);
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set("calculate", Napi::Function::New(env, Calculate));
    return exports;
}

NODE_API_MODULE(calculator, Init)
