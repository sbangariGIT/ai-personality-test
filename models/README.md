# Sample Question Benchmarking

## Overview

This directory contains scripts and data used to run sample questions on various language models for benchmarking purposes. The goal is to compare the performance of different models and assess their capabilities in generating accurate, coherent, and contextually relevant responses.

## Models Under Comparison

Currently, we are benchmarking the following models:

1. **OpenAI GPT-3.5-turbo**
2. **OpenAI GPT-4**
3. **Perplexity Llama-3-sonar-large-32k-online**
4. **Anthropic Claude-3-5-sonnet-20240620**
5. **Marcus-v0** (Our home-grown solution)

## Directory Structure

- `anthropicAI/`: Contains scripts to run sample questions on each model.
- `marcus/`: Includes sample questions and expected outputs for benchmarking.
- `openAI/`: Stores the results of the benchmarks for comparison.
- `perplexityAI/`: Stores the results of the benchmarks for comparison.
- `utils/`: This contains keys.py and google_sheets.json for API keys and URLS that are needed to write the benchmarks

## Running Benchmarks

To run the benchmarks, execute the main.py. Ensure you have the necessary API keys and dependencies installed before running the script.

### Example

```sh
# Run the benchmark script
python main.py
```

### Viewing Benchmarks

The benchmark results are available at this file: https://docs.google.com/spreadsheets/d/1aCqGhClgLGn0H7PJAQkQsEQktkAqJGSlLz-AT4N_qIQ/edit?gid=0#gid=0
Please request access only in the event where you really need it, approval time varies based on my (sbangariGIT) availability. Ping me on slack if its urgent