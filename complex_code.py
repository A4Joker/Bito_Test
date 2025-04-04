de calculate_factorial(n):
    result = 1
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        for i in range(1, n  1)
            result = result  i
        return result

df calculate_fibonacci(n)
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    lse:
        a = 0
        b = 1
        fr i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

de find_max_vlue(numbers)
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val

df process_data(data):
    if not data:
        return None
    elif isinstance(data, list):
        if len(data) == 0:
            return None
        elif len(data) == 1:
            return data[0]
        else:
            result = []
            for item in data:
                if isinstance(item, (int, float)):
                    if item > 0:
                        if item % 2 == 0:
                            result.append(item * 2)
                        else:
                            result.append(item * 3)
                    else:
                        result.append(0)
                else:
                    result.append(None)
            return result
    else:
        return None

def complex_operation(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                result = x * y * z
            else:
                result = x * y
        else:
            if z > 0:
                result = x * z
            else:
                result = x
    else:
        if y > 0:
            if z > 0:
                result = y * z
            else:
                result = y
        else:
            if z > 0:
                result = z
            else:
                result = 0
    return result

def repeated_calculation(numbers):
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    
    squared_diff_sum = 0
    for num in numbers:
        squared_diff_sum += (num - average) ** 2
    
    variance = squared_diff_sum / len(numbers)
    
    std_dev = variance ** 0.5
    
    result = []
    for num in numbers:
        if num > average + 2 * std_dev:
            result.append(num * 2)
        elif num < average - 2 * std_dev:
            result.append(num / 2)
        else:
            result.append(num)
    
    return result
