% No proper header comment block
function results = data_processor(input_data, params)
    % Global variables
    global CONSTANTS;
    global debug_mode;
    
    % Magic numbers throughout the code
    if nargin < 2
        params = struct('iterations', 1000, 'threshold', 0.001, 'method', 'fast');
    end
    
    % No input validation
    
    % Poor variable naming
    x = input_data;
    p = params;
    
    % Unvectorized code with growing arrays
    res = [];
    for i = 1:length(x)
        % Magic numbers
        if x(i) > 10
            val = process_value(x(i), 2.5, 0.3);
        else
            val = x(i) * 1.5;
        end
        
        % Growing array inside loop
        res = [res; val];
    end
    
    % Inconsistent indentation and formatting
    if p.method == 'fast'
        % No pre-allocation
    filtered_data = [];
    for i = 1:length(res)
        if res(i) > p.threshold
            filtered_data = [filtered_data; res(i)];
        end
    end
    else
        % Poor error handling
        try
            filtered_data = advanced_filter(res, p.threshold);
        catch
            disp('Error in advanced filter, using basic filter');
            filtered_data = res(res > p.threshold);
        end
    end
    
    % Nested conditionals without early returns
    if ~isempty(filtered_data)
        if p.iterations > 0
            if strcmp(p.method, 'fast')
                % Deeply nested code
                iter_results = zeros(length(filtered_data), p.iterations);
                for it = 1:p.iterations
                    for j = 1:length(filtered_data)
                        % Magic calculation without explanation
                        iter_results(j, it) = filtered_data(j) * (1 - 0.01 * it);
                    end
                end
                final_result = mean(iter_results, 2);
            else
                % Direct floating-point comparison
                if p.threshold == 0.001
                    final_result = filtered_data .* 0.75;
                else
                    final_result = filtered_data .* 0.85;
                end
            end
        else
            final_result = filtered_data;
        end
    else
        final_result = [];
    end
    
    % Poor memory management with struct fields
    results = struct();
    results.processed = res;
    results.filtered = filtered_data;
    results.final = final_result;
    results.params = p;
    
    % Debugging code left in production
    if debug_mode
        figure;
        plot(1:length(res), res, 'r-', 1:length(final_result), final_result, 'b--');
        title('Processing Results');
        legend('Raw', 'Final');
    end
    
    % Nested function without clear purpose
    function output = process_value(input, factor1, factor2)
        % No comments explaining the algorithm
        temp = input * factor1;
        if temp > 20
            output = temp - factor2 * sqrt(temp);
        else
            output = temp + factor2 * temp^2;
        end
        
        % Unnecessary global variable access
        if CONSTANTS.VERBOSE
            fprintf('Processed value %f to %f\n', input, output);
        end
    end
end

% Separate function in the same file (violates one function per file)
function result = advanced_filter(data, thresh)
    % Poor variable naming
    t = thresh;
    d = data;
    
    % Inefficient algorithm
    result = [];
    for i = 1:length(d)
        if i > 1 && i < length(d)
            % Magic numbers and complex condition
            if d(i) > t && (d(i) > d(i-1) * 1.2 || d(i) > d(i+1) * 1.2)
                result = [result; d(i)];
            end
        end
    end
    
    % No error handling for edge cases
end

% Script-like code at the end of the file
test_data = rand(100, 1) * 20;
test_params = struct('iterations', 500, 'threshold', 0.002, 'method', 'detailed');
results = data_processor(test_data, test_params);
disp('Processing complete');
