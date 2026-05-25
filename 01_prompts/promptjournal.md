
What you asked AI. What AI gave you. Whether the answer was useful. What you understood from the answer.

Prompt 1: Code Generation 

Prompt Used:  I am a beginner Python student. Please create a simple Python function that gives square root of any number. Keep the code easy to understand. Add short comments. After the code, explain how it works in simple words.

AI Output Summary: The code uses python math library to use math.sqrt function to calculate square root of any give number. 

Was it useful? Yes 

What I understood: we can import predefined libraries and use functions from them in python.



Prompt 2    : Code Generation 

Prompt Used:  Explain the square root calculator function in beginner friendly language line by line so that i get my foundations clear.

AI Output Summary: It explained the importance and working of libraries and functions in python. 

Was it useful? Yes 

What I understood: we can use functions to implement repetitive code in python.



Prompt 3   : Debugging

Prompt Used:  import math

def square_root(number):
  
    if number < 0 
    raise ValueError("Square root is not defined for negative numbers.") 

    return Math.sqrt(number) 

i wrote this code to calculate square root of any number but it has error, debug the code and explain it in beginner friendly language


AI Output Summary: Ai found out the syntax error in my code, colon(:) in if statements, indentation in python and the uppercase0 Math 

Was it useful? Yes 

What I understood: Python is case sensitive, Indentation is important and colons and other symbols are important.




Prompt 4   : Optimization
Prompt Used:  how can i make square root function cleaner saer and easier to read?

AI Output Summary: It explained why things like better spacing, hints, documentation, imput type and other important issues can help other people to read the code and make it clear for everyone and scalable. 

Was it useful? Yes 

What I understood: Good code is Easy to read
Easy to debug
Safe against mistakes
Easy to maintain.




Prompt 5   : Testing
Prompt Used:  generate pytest for my square root function for every possible use case

AI Output Summary: Testing is important to check if out code works properly, works for edge cases and does not crash.

Was it useful? Yes 

What I understood: How pytest works and We need to check Cevery type of input for our code.














<!-- # Generative AI Prompt Journal

This file tracks production-ready prompts, system instructions, and engineering guidelines for AI-assisted development.

## 🛠️ System Rules & Global Context
* **Code Quality:** Write clean, modular, and self-documenting code.
* **Typing:** Use strict typing (e.g., TypeScript, Python type hints). No implicit `any` or loose types.
* **Style:** Follow industry-standard style guides (PEP 8, Prettier, etc.).
* **Output:** Provide only the requested code block or explanation. Avoid conversational filler like "Sure, here is your code."

---

## 📋 Prompt Logs

### 1. Code Generation
* **Goal:** Generate structured, production-ready code blocks from feature descriptions.
* **Prompt:**
```text
Act as an expert software engineer. Generate a modular, strictly-typed [LANGUAGE] function for the following feature: [FEATURE_DESCRIPTION].

Requirements:
- Input parameters: [INPUTS]
- Expected output: [OUTPUTS]
- Use modern best practices and include JSDoc/Docstring documentation.
- Handle edge cases, including null, undefined, or empty inputs.
- Output ONLY the code block. Do not include introductory text.
```

### 2. Code Explanation
* **Goal:** Break down complex codebases, legacy code, or regex for onboarding and code reviews.
* **Prompt:**
```text
Act as a technical architect. Analyze the provided [LANGUAGE] code snippet and explain its functionality to a junior developer.

Structure your response as follows:
1. **High-Level Summary:** What does this code do in 2 sentences?
2. **Step-by-Step Breakdown:** Bullet points explaining the logic chronologically.
3. **Complexity Analysis:** State the Time and Space complexity using Big O notation.
4. **Key Assumptions:** Note any dependencies or assumptions made by the code.

Here is the code:
[PASTE_CODE_HERE]
```

### 3. Debugging & Error Resolution
* **Goal:** Identify root causes of failures and provide robust, permanent fixes.
* **Prompt:**
```text
Act as a principal debugging engineer. Review the following [LANGUAGE] code and its corresponding error message/unexpected behavior.

Context:
- Expected behavior: [EXPECTED_BEHAVIOR]
- Actual behavior / Error message: [ERROR_OR_BUG_DESCRIPTION]

Code Snippet:
[PASTE_CODE_HERE]

Tasks:
1. Identify the root cause of the bug.
2. Provide the corrected code block.
3. Explain why the fix works and how to prevent this issue in the future.
```

### 4. Performance Optimization
* **Goal:** Reduce execution time, memory footprints, or cloud computing costs.
* **Prompt:**
```text
Act as a performance tuning specialist. Optimize the following [LANGUAGE] code for [METRIC: e.g., Execution Time / Memory Usage / API Calls].

Current Code:
[PASTE_CODE_HERE]

Constraints:
- Do not change the function signature or break existing functionality.
- Prioritize readability unless it severely impacts performance.

Provide:
1. Optimized code block.
2. Comparative analysis of the old vs. new Time/Space complexity.
3. Explanation of the optimization techniques used (e.g., caching, vectorization, algorithmic change).
```

### 5. Automated Test Generation
* **Goal:** Generate comprehensive unit tests to ensure high test coverage and regression prevention.
* **Prompt:**
```text
Act as a QA automation engineer. Write a comprehensive suite of unit tests for the provided [LANGUAGE] code using the [TESTING_FRAMEWORK] library.

Code to test:
[PASTE_CODE_HERE]

Test Suite Requirements:
- Write tests for happy path scenarios.
- Write tests for boundary values and edge cases (e.g., empty strings, negative numbers, extreme inputs).
- Write tests for explicit error handling and exceptions.
- Use mock data or spies for external dependencies if applicable.
- Ensure clear, descriptive test names (e.g., `it("should throw an error when input is negative")`).
``` -->