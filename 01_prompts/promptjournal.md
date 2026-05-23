# Generative AI Prompt Journal

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
```
