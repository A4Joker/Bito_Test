// native/processor.cpp
#include <napi.h>
#include <string>
#include <vector>

class FileProcessor : public Napi::ObjectWrap<FileProcessor> {
public:
    static Napi::Object Init(Napi::Env env, Napi::Object exports) {
        Napi::Function func = DefineClass(env, "FileProcessor", {
            InstanceMethod("processBuffer", &FileProcessor::ProcessBuffer),
            InstanceMethod("analyze", &FileProcessor::Analyze)
        });
        
        exports.Set("FileProcessor", func);
        return exports;
    }

    FileProcessor(const Napi::CallbackInfo& info) 
        : Napi::ObjectWrap<FileProcessor>(info) {}

private:
    Napi::Value ProcessBuffer(const Napi::CallbackInfo& info) {
        Napi::Env env = info.Env();
        
        if (!info[0].IsBuffer()) {
            throw Napi::Error::New(env, "Expected buffer as argument");
        }

        Napi::Buffer<uint8_t> buffer = info[0].As<Napi::Buffer<uint8_t>>();
        size_t length = buffer.Length();
        uint8_t* data = buffer.Data();

        // Process the buffer
        std::vector<uint8_t> processed(data, data + length);
        for (size_t i = 0; i < length; i++) {
            processed[i] = processed[i] * 2; // Simple transformation
        }

        return Napi::Buffer<uint8_t>::Copy(env, processed.data(), processed.size());
    }

    Napi::Value Analyze(const Napi::CallbackInfo& info) {
        Napi::Env env = info.Env();
        
        if (!info[0].IsString()) {
            throw Napi::Error::New(env, "Expected string as argument");
        }

        std::string input = info[0].As<Napi::String>();
        
        // Perform analysis
        size_t wordCount = std::count(input.begin(), input.end(), ' ') + 1;
        
        Napi::Object result = Napi::Object::New(env);
        result.Set("wordCount", Napi::Number::New(env, wordCount));
        result.Set("length", Napi::Number::New(env, input.length()));
        
        return result;
    }
};

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    return FileProcessor::Init(env, exports);
}

NODE_API_MODULE(processor, Init)
