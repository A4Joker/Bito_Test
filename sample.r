# Missing package documentation
library(dplyr)
library(ggplot2)
library(readr)

# Using = for assignment instead of <- (Violates Generative Prompt #4)
max_iterations = 100
default_threshold = 0.001

# Magic numbers without constants (Violates Generative Prompt #8)
if (runif(1) > 0.75) {
  message("High random value detected")
}

# Global variables (Violates Generative Prompt #7)
all_results = list()
error_count = 0

# This global variable should be ignored by CRA due to cleanup prompt #7
.G_AppConfig = list(
  version = "1.2.3",
  debug = FALSE,
  max_threads = 4
)

# Function without proper documentation (Violates Generative Prompt #2)
processData = function(data, threshold = 0.05, iterations = 10) {
  # Inconsistent naming (camelCase instead of snake_case) (Violates Generative Prompt #3)
  dataSize = nrow(data)
  
  # Using T instead of TRUE (Violates Generative Prompt #17)
  useWeights = T
  
  # Poor error handling without tryCatch (Violates Generative Prompt #6)
  if (is.null(data)) {
    stop("Data is NULL")
  }
  
  # Loop instead of vectorization (Violates Generative Prompt #9)
  results = c()
  for (i in 1:dataSize) {
    value = data[i, "value"]
    if (!is.na(value)) {
      results = c(results, value * 2)
    } else {
      results = c(results, 0)
    }
  }
  
  # This loop should be ignored by CRA due to cleanup prompt #3
  #' @performance:loop-required
  specialResults = c()
  for (i in 1:length(results)) {
    # This loop is required for special sequential processing
    specialResults[i] = complex_calculation(results[i], i)
  }
  
  # Poor string concatenation (Violates Generative Prompt #18)
  message("Processed " + dataSize + " records")
  
  # Returning multiple values via global variable (Violates Generative Prompt #19)
  all_results[[length(all_results) + 1]] = results
  
  return(mean(results))
}

# This function should be ignored by CRA due to cleanup prompt #2
.internal_helper = function(x, y) {
  # Internal helper function with non-standard naming
  return(x * y + runif(1))
}

# Function with poor error handling (Violates Generative Prompt #6)
calculateStatistics = function(data) {
  # Suppressing warnings instead of handling them
  result = suppressWarnings({
    mean_val = mean(data$value)
    sd_val = sd(data$value)
    median_val = median(data$value)
    
    return(list(mean = mean_val, sd = sd_val, median = median_val))
  })
  
  return(result)
}

# This error handling section should be ignored by CRA due to cleanup prompt #5
#' @error:custom-handling
customErrorProcess = function(expr) {
  result = NULL
  error = NULL
  
  # Custom error handling approach
  result = try(expr, silent = TRUE)
  if (inherits(result, "try-error")) {
    error = as.character(result)
    result = NULL
  }
  
  return(list(result = result, error = error))
}

# Function that's too long (Violates Generative Prompt #5)
analyzeDataset = function(file_path, options = list()) {
  # Over 50 lines of code in a single function
  # Default options
  if (is.null(options$header)) options$header = TRUE
  if (is.null(options$sep)) options$sep = ","
  if (is.null(options$filter)) options$filter = NULL
  if (is.null(options$transform)) options$transform = NULL
  if (is.null(options$analyze)) options$analyze = "all"
  if (is.null(options$output)) options$output = "summary"
  
  # Read data
  data = read.csv(file_path, header = options$header, sep = options$sep)
  
  # Filter data
  if (!is.null(options$filter)) {
    # This uses = instead of <- but should be ignored due to cleanup prompt #6
    #' @style:assignment-equals
    filtered_data = subset(data, eval(parse(text = options$filter)))
  } else {
    filtered_data = data
  }
  
  # Transform data
  if (!is.null(options$transform)) {
    for (transform in options$transform) {
      if (transform$type == "scale") {
        filtered_data[[transform$column]] = scale(filtered_data[[transform$column]])
      } else if (transform$type == "log") {
        filtered_data[[transform$column]] = log(filtered_data[[transform$column]] + 1)
      } else if (transform$type == "categorical") {
        filtered_data[[transform$column]] = as.factor(filtered_data[[transform$column]])
      }
    }
  }
  
  # Analyze data
  results = list()
  
  # Poor NA handling (Violates Generative Prompt #11)
  numeric_columns = sapply(filtered_data, is.numeric)
  if (any(numeric_columns)) {
    numeric_data = filtered_data[, numeric_columns]
    results$numeric = list(
      mean = apply(numeric_data, 2, mean),
      median = apply(numeric_data, 2, median),
      sd = apply(numeric_data, 2, sd),
      min = apply(numeric_data, 2, min),
      max = apply(numeric_data, 2, max)
    )
  }
  
  # This NA handling section should be ignored by CRA due to cleanup prompt #9
  #' @na:special-handling
  special_columns = c("treatment", "response")
  if (all(special_columns %in% names(filtered_data))) {
    # Special handling for treatment-response analysis
    # NA values have domain-specific meaning here
    tr_data = filtered_data[, special_columns]
    results$treatment_effect = analyze_treatment_effect(tr_data)
  }
  
  # Categorical analysis
  factor_columns = sapply(filtered_data, is.factor)
  if (any(factor_columns)) {
    factor_data = filtered_data[, factor_columns]
    results$categorical = lapply(factor_data, table)
  }
  
  # Correlation analysis
  if (sum(numeric_columns) > 1) {
    results$correlation = cor(numeric_data, use = "pairwise.complete.obs")
  }
  
  # Generate output
  if (options$output == "summary") {
    print_summary(results)
  } else if (options$output == "full") {
    return(results)
  } else if (options$output == "plot") {
    generate_plots(filtered_data, results)
  }
  
  # More code...
  # (imagine this function continues for many more lines)
  
  return(results)
}

# This legacy function should be ignored by CRA due to cleanup prompt #1
#' @legacy
OldProcessFunc <- function(Data, Options) {
  # Legacy function with inconsistent naming and style
  Results <- list()
  
  # Legacy implementation...
  
  return(Results)
}

# Poor argument validation (Violates Generative Prompt #12)
plot_results = function(data, type) {
  # Missing argument validation
  
  if (type == "histogram") {
    hist(data$value, main = "Histogram of Values", xlab = "Value")
  } else if (type == "scatter") {
    plot(data$x, data$y, main = "Scatter Plot", xlab = "X", ylab = "Y")
  } else if (type == "boxplot") {
    boxplot(data$value ~ data$group, main = "Boxplot by Group")
  }
}

# These variables should be ignored by CRA due to cleanup prompt #4
#' @naming:retain
UserPrefs = list()
DefaultOpts = list(width = 10, height = 8)

# This data visualization section should be ignored by CRA due to cleanup prompt #10
#' @dataframe:direct-access
create_visualization = function(data) {
  # Direct $ notation is preferred in visualization code for readability
  p = ggplot(data, aes(x = data$x, y = data$y, color = data$group)) +
    geom_point() +
    labs(title = "Data Visualization",
         x = "X Axis",
         y = "Y Axis",
         color = "Group")
  
  return(p)
}

# Main execution code with poor organization (Violates Generative Prompt #16)
set.seed(123)

# Generate sample data
sample_data = data.frame(
  id = 1:100,
  value = rnorm(100),
  group = sample(c("A", "B", "C"), 100, replace = TRUE),
  x = runif(100),
  y = runif(100)
)

# Process data
result = processData(sample_data)
print(paste0("Result: ", result))

# Calculate statistics
stats = calculateStatistics(sample_data)
print(stats)

# Inconsistent indentation (Violates Generative Prompt #14)
if(result > 0) {
message("Positive result")
  # More code...
} else {
  message("Non-positive result")
    # More code with inconsistent indentation
}

# Function to perform a complex calculation
complex_calculation = function(value, index) {
  # Magic number (Violates Generative Prompt #8)
  if (value > 1.5) {
    return(value * index / 2.75)
  } else {
    return(value * index * 0.85)
  }
}

# Save results
write.csv(sample_data, "results.csv", row.names = FALSE)
