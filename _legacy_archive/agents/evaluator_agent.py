# # agents/evaluator_agent.py
# import traceback

# def evaluator_agent():
#     def evaluate(inputs):
#         code = inputs["code"]
#         problem = inputs["problem"].lower()

#         local_env = {}
#         test_results = []

#         try:
#             exec(code, {}, local_env)

#             # -------------------------------
#             # LONGEST PALINDROMIC SUBSTRING
#             # -------------------------------
#             if "palindromic substring" in problem:
#                 if "longestPalindrome" not in local_env:
#                     return {
#                         "passed": False,
#                         "error": "Function longestPalindrome not found",
#                         "failed_test": "Function existence check",
#                         "expected": "Function longestPalindrome",
#                         "got": "Function not found",
#                         "test_results": []
#                     }

#                 fn = local_env["longestPalindrome"]
#                 tests = [
#                     ("babad", ("bab", "aba"), "Should return 'bab' or 'aba'"),
#                     ("cbbd", "bb", "Should return 'bb'"),
#                     ("a", "a", "Single character"),
#                     ("", "", "Empty string")
#                 ]
                
#                 for test_input, expected, description in tests:
#                     try:
#                         result = fn(test_input)
#                         if isinstance(expected, tuple):
#                             passed = result in expected
#                         else:
#                             passed = result == expected
#                         test_results.append({
#                             "test": f"longestPalindrome({repr(test_input)})",
#                             "description": description,
#                             "expected": expected,
#                             "got": result,
#                             "passed": passed
#                         })
#                         if not passed:
#                             return {
#                                 "passed": False,
#                                 "error": f"Test failed: {description}",
#                                 "failed_test": f"longestPalindrome({repr(test_input)})",
#                                 "expected": expected,
#                                 "got": result,
#                                 "test_results": test_results
#                             }
#                     except Exception as e:
#                         return {
#                             "passed": False,
#                             "error": f"Test error: {str(e)}",
#                             "failed_test": f"longestPalindrome({repr(test_input)})",
#                             "expected": expected,
#                             "got": f"Exception: {str(e)}",
#                             "test_results": test_results
#                         }

#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": test_results
#                 }

#             # -------------------------------
#             # CLIMBING STAIRS
#             # -------------------------------
#             if "climb" in problem and "stair" in problem:
#                 if "climbStairs" not in local_env:
#                     # Try alternative function names
#                     for alt_name in ["count_ways", "climb_stairs", "ways_to_climb"]:
#                         if alt_name in local_env:
#                             fn = local_env[alt_name]
#                             break
#                     else:
#                         return {
#                             "passed": False,
#                             "error": "Function climbStairs (or count_ways/climb_stairs/ways_to_climb) not found",
#                             "failed_test": "Function existence check",
#                             "expected": "Function climbStairs or similar",
#                             "got": "Function not found",
#                             "test_results": []
#                         }
#                 else:
#                     fn = local_env["climbStairs"]

#                 tests = [
#                     (1, 1, "1 stair = 1 way"),
#                     (2, 2, "2 stairs = 2 ways"),
#                     (3, 3, "3 stairs = 3 ways"),
#                     (5, 8, "5 stairs = 8 ways")
#                 ]
                
#                 for test_input, expected, description in tests:
#                     try:
#                         result = fn(test_input)
#                         passed = result == expected
#                         test_results.append({
#                             "test": f"climbStairs({test_input})",
#                             "description": description,
#                             "expected": expected,
#                             "got": result,
#                             "passed": passed
#                         })
#                         if not passed:
#                             return {
#                                 "passed": False,
#                                 "error": f"Test failed: {description}",
#                                 "failed_test": f"climbStairs({test_input})",
#                                 "expected": expected,
#                                 "got": result,
#                                 "test_results": test_results
#                             }
#                     except Exception as e:
#                         return {
#                             "passed": False,
#                             "error": f"Test error: {str(e)}",
#                             "failed_test": f"climbStairs({test_input})",
#                             "expected": expected,
#                             "got": f"Exception: {str(e)}",
#                             "test_results": test_results
#                         }

#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": test_results
#                 }

#             # -------------------------------
#             # REVERSE LINKED LIST
#             # -------------------------------
#             if "reverse linked list" in problem:
#                 if "reverseList" not in local_env:
#                     return {
#                         "passed": False,
#                         "error": "Function reverseList not found",
#                         "failed_test": "Function existence check",
#                         "expected": "Function reverseList",
#                         "got": "Function not found",
#                         "test_results": []
#                     }

#                 # Structural correctness only (runtime safety)
#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": [{"test": "Function exists", "passed": True}]
#                 }

#             # -------------------------------
#             # LONGEST COMMON SUBSEQUENCE
#             # -------------------------------
#             if "longest common subsequence" in problem or "lcs" in problem:
#                 if "longestCommonSubsequence" not in local_env:
#                     return {
#                         "passed": False,
#                         "error": "Function longestCommonSubsequence not found",
#                         "failed_test": "Function existence check",
#                         "expected": "Function longestCommonSubsequence",
#                         "got": "Function not found",
#                         "test_results": []
#                     }

#                 fn = local_env["longestCommonSubsequence"]
#                 tests = [
#                     (("abcde", "ace"), 3, "Basic LCS"),
#                     (("abc", "abc"), 3, "Identical strings"),
#                     (("abc", "def"), 0, "No common subsequence")
#                 ]
                
#                 for test_input, expected, description in tests:
#                     try:
#                         result = fn(*test_input)
#                         passed = result == expected
#                         test_results.append({
#                             "test": f"longestCommonSubsequence{test_input}",
#                             "description": description,
#                             "expected": expected,
#                             "got": result,
#                             "passed": passed
#                         })
#                         if not passed:
#                             return {
#                                 "passed": False,
#                                 "error": f"Test failed: {description}",
#                                 "failed_test": f"longestCommonSubsequence{test_input}",
#                                 "expected": expected,
#                                 "got": result,
#                                 "test_results": test_results
#                             }
#                     except Exception as e:
#                         return {
#                             "passed": False,
#                             "error": f"Test error: {str(e)}",
#                             "failed_test": f"longestCommonSubsequence{test_input}",
#                             "expected": expected,
#                             "got": f"Exception: {str(e)}",
#                             "test_results": test_results
#                         }

#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": test_results
#                 }

#             # -------------------------------
#             # SLIDING WINDOW MAXIMUM
#             # -------------------------------
#             if "sliding window maximum" in problem:
#                 if "maxSlidingWindow" not in local_env:
#                     return {
#                         "passed": False,
#                         "error": "Function maxSlidingWindow not found",
#                         "failed_test": "Function existence check",
#                         "expected": "Function maxSlidingWindow",
#                         "got": "Function not found",
#                         "test_results": []
#                     }

#                 fn = local_env["maxSlidingWindow"]
#                 test_input = ([1,3,-1,-3,5,3,6,7], 3)
#                 expected = [3,3,5,5,6,7]
                
#                 try:
#                     result = fn(*test_input)
#                     passed = result == expected
#                     test_results.append({
#                         "test": f"maxSlidingWindow{test_input}",
#                         "description": "Sliding window maximum",
#                         "expected": expected,
#                         "got": result,
#                         "passed": passed
#                     })
#                     if not passed:
#                         return {
#                             "passed": False,
#                             "error": "Test failed: Sliding window maximum",
#                             "failed_test": f"maxSlidingWindow{test_input}",
#                             "expected": expected,
#                             "got": result,
#                             "test_results": test_results
#                         } 
#                 except Exception as e:
#                     return {
#                         "passed": False,
#                         "error": f"Test error: {str(e)}",
#                         "failed_test": f"maxSlidingWindow{test_input}",
#                         "expected": expected,
#                         "got": f"Exception: {str(e)}",
#                         "test_results": test_results
#                     }

#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": test_results
#                 }

#             # -------------------------------
#             # TASK DEPENDENCY / TOPOLOGICAL SORT
#             # -------------------------------

#             if "task" in problem and "depend" in problem:
#                 # Accept multiple possible function names
#                 fn_names = ["canFinishTasks", "canFinish", "findOrder"]
#                 for name in fn_names:
#                     if name in local_env:
#                         fn = local_env[name]
#                         break
#                 else:
#                     return {
#                         "passed": False,
#                         "error": f"Function {fn_names} not found",
#                         "failed_test": "Function existence check",
#                         "expected": "Function to determine task execution order",
#                         "got": "Function not found",
#                         "test_results": []
#                     }

#                 tests = [
#                     ((4, [[1,0],[2,1],[3,2]]), (True, [0,1,2,3]), "Linear dependency chain"),
#                     ((2, [[0,1],[1,0]]), (False, []), "Cyclic dependency")
#                 ]

#                 for (numTasks, deps), expected, description in tests:
#                     try:
#                         result = fn(numTasks, deps)
#                         passed = result[0] == expected[0]

#                         test_results.append({
#                             "test": f"{fn.__name__}({numTasks}, {deps})",
#                             "description": description,
#                             "expected": expected,
#                             "got": result,
#                             "passed": passed
#                         })

#                         if not passed:
#                             return {
#                                 "passed": False,
#                                 "error": f"Test failed: {description}",
#                                 "failed_test": description,
#                                 "expected": expected,
#                                 "got": result,
#                                 "test_results": test_results
#                             }

#                     except Exception as e:
#                         return {
#                             "passed": False,
#                             "error": f"Execution error: {str(e)}",
#                             "failed_test": description,
#                             "expected": expected,
#                             "got": f"Exception: {str(e)}",
#                             "test_results": test_results
#                         }

#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": test_results
#                 }


#             # -------------------------------
#             # FALLBACK (Unknown problem)
#             # -------------------------------
#             return {
#                 "passed": True,
#                 "error": None,
#                 "test_results": [{"test": "No specific tests", "passed": True, "description": "Unknown problem type"}]
#             }

#         except SyntaxError as e:
#             return {
#                 "passed": False,
#                 "error": f"Syntax Error: {str(e)}\n{traceback.format_exc()}",
#                 "failed_test": "Code syntax check",
#                 "expected": "Valid Python syntax",
#                 "got": f"SyntaxError: {str(e)}",
#                 "test_results": []
#             }
#         except Exception as e:
#             return {
#                 "passed": False,
#                 "error": traceback.format_exc(),
#                 "failed_test": "Code execution",
#                 "expected": "Successful execution",
#                 "got": f"Exception: {str(e)}",
#                 "test_results": []
#             }

#     return evaluate


# -------------------------------------------------------
# import json
# import traceback
# from util.llm import get_llm

# def evaluator_agent():
#     llm = get_llm(role="reviewer")

#     def evaluate(inputs):
#         code = inputs["code"]
#         problem = inputs["problem"]

#         # ---------- LLM generates test plan ----------
#         try:
#             prompt = f"""
# Problem:
# {problem}

# Code:
# {code}

# Generate evaluation tests as instructed.
# """
#             response = llm.invoke(prompt)
#             test_spec = json.loads(response.content)
#         except Exception as e:
#             return {
#                 "passed": False,
#                 "error": f"Evaluator LLM failed: {str(e)}",
#                 "test_results": []
#             }

#         # ---------- Execute tests ----------
#         local_env = {}
#         results = []

#         try:
#             exec(code, {}, local_env)

#             for t in test_spec["tests"]:
#                 try:
#                     actual = eval(t["call"], {}, local_env)
#                     passed = actual == t["expected"]
#                 except Exception as ex:
#                     actual = str(ex)
#                     passed = False

#                 results.append({
#                     "test": t["call"],
#                     "description": t["description"],
#                     "expected": t["expected"],
#                     "got": actual,
#                     "passed": passed
#                 })

#                 if not passed:
#                     return {
#                         "passed": False,
#                         "error": "One or more tests failed",
#                         "test_results": results
#                     }

#             return {
#                 "passed": True,
#                 "error": None,
#                 "test_results": results
#             }

#         except Exception as e:
#             return {
#                 "passed": False,
#                 "error": traceback.format_exc(),
#                 "test_results": results
#             }

#     return evaluate
# ----------------------------------------


# import json
# import re
# import traceback
# from util.llm import get_llm


# def evaluator_agent():
#     """
#     Hybrid execution-based evaluator.

#     Priority order:
#     1. Deterministic manual tests for known benchmark problems
#     2. LLM-generated tests for unseen problems (fallback)
#     """

#     llm = get_llm(role="reviewer")

#     # ---------------------------------------------------------
#     # Utility: Safe JSON extraction from LLM output
#     # ---------------------------------------------------------
#     def safe_parse_json(text: str):
#         text = text.strip()
#         try:
#             return json.loads(text)
#         except Exception:
#             pass

#         match = re.search(r"\{.*\}", text, re.DOTALL)
#         if not match:
#             return None

#         try:
#             return json.loads(match.group())
#         except Exception:
#             return None

#     # ---------------------------------------------------------
#     # Utility: Check if a topological order is valid
#     # ---------------------------------------------------------
#     def is_valid_order(numTasks, deps, order):
#         if not order or len(order) != numTasks:
#             return False
#         pos = {task: i for i, task in enumerate(order)}
#         for dest, src in deps:
#             if pos[src] > pos[dest]:
#                 return False
#         return True

#     # ---------------------------------------------------------
#     # Main evaluation function
#     # ---------------------------------------------------------
#     def evaluate(inputs):
#         code = inputs["code"]
#         problem = inputs["problem"].lower()

#         local_env = {}
#         test_results = []

#         # -----------------------------------------------------
#         # STEP 1: Execute generated code
#         # -----------------------------------------------------
#         try:
#             exec(code, {}, local_env)
#         except Exception:
#             return {
#                 "passed": False,
#                 "error": "Generated code failed to execute",
#                 "traceback": traceback.format_exc(),
#                 "test_results": []
#             }

#         # =====================================================
#         # MANUAL BENCHMARK EVALUATORS
#         # =====================================================

#         # -----------------------------------------------------
#         # CLIMBING STAIRS (Dynamic Programming)
#         # -----------------------------------------------------
#         if "climb" in problem and "stair" in problem:
#             fn = None
#             for name in ["climbStairs", "climb_stairs", "count_ways", "ways_to_climb"]:
#                 if name in local_env:
#                     fn = local_env[name]
#                     break

#             if fn is None:
#                 return {
#                     "passed": False,
#                     "error": "No valid climbing stairs function found",
#                     "test_results": []
#                 }

#             tests = [
#                 (1, 1, "1 stair = 1 way"),
#                 (2, 2, "2 stairs = 2 ways"),
#                 (3, 3, "3 stairs = 3 ways"),
#                 (5, 8, "5 stairs = 8 ways"),
#             ]

#             for n, expected, desc in tests:
#                 try:
#                     result = fn(n)
#                     passed = result == expected
#                 except Exception as e:
#                     result = f"Exception: {str(e)}"
#                     passed = False

#                 test_results.append({
#                     "test": f"{fn.__name__}({n})",
#                     "description": desc,
#                     "expected": expected,
#                     "got": result,
#                     "passed": passed
#                 })

#                 if not passed:
#                     return {
#                         "passed": False,
#                         "error": "One or more tests failed",
#                         "test_results": test_results
#                     }

#             return {
#                 "passed": True,
#                 "error": None,
#                 "test_results": test_results
#             }

#         # -----------------------------------------------------
#         # TASK DEPENDENCY / TOPOLOGICAL SORT
#         # -----------------------------------------------------
#         if ("tasks" in problem and "dependencies") or "findOrder" in problem:
#             fn = None
#             for name in ["findOrder", "canFinish", "canFinishTasks"]:
#                 if name in local_env:
#                     fn = local_env[name]
#                     break

#             if fn is None:
#                 return {
#                     "passed": False,
#                     "error": "No task dependency function found",
#                     "test_results": []
#                 }

#             # ---------------------------
#             # 6 manual test cases
#             # ---------------------------
#             tests = [
#                 ("Linear chain", (4, [[1, 0], [2, 1], [3, 2]]), [0, 1, 2, 3]),
#                 ("Cycle detection", (2, [[0, 1], [1, 0]]), []),
#                 ("Branching dependencies", (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), None),  # any valid order
#                 ("No dependencies", (3, []), [0, 1, 2]),
#                 ("Single task", (1, []), [0]),
#                 ("Complex cycle", (4, [[0,1],[1,2],[2,3],[3,1]]), [])
#             ]

#             for desc, args, expected in tests:
#                 try:
#                     result = fn(*args)
#                     if expected is None:  # multiple valid orders allowed
#                         passed = is_valid_order(*args, result)
#                     else:
#                         passed = result == expected
#                 except Exception as e:
#                     result = f"Exception: {str(e)}"
#                     passed = False

#                 test_results.append({
#                     "test": f"{fn.__name__}{args}",
#                     "description": desc,
#                     "expected": expected if expected is not None else "Any valid topological order",
#                     "got": result,
#                     "passed": passed
#                 })

#                 if not passed:
#                     return {
#                         "passed": False,
#                         "error": "One or more tests failed",
#                         "test_results": test_results
#                     }

#             return {
#                 "passed": True,
#                 "error": None,
#                 "test_results": test_results
#             }

#         # =====================================================
#         # HYBRID FALLBACK: LLM-GENERATED TESTS
#         # =====================================================
#         try:
#             prompt = f"""
# Problem:
# {inputs["problem"]}

# Code:
# {code}

# Generate evaluation tests strictly in JSON as instructed.
# """
#             response = llm.invoke(prompt)
#             test_spec = safe_parse_json(response.content)

#             if not test_spec or "tests" not in test_spec:
#                 return {
#                     "passed": True,
#                     "error": None,
#                     "test_results": [{
#                         "test": "Smoke test",
#                         "description": "Code executed without runtime errors",
#                         "passed": True
#                     }]
#                 }

#         except Exception:
#             return {
#                 "passed": True,
#                 "error": None,
#                 "test_results": [{
#                     "test": "Smoke test",
#                     "description": "Code executed without runtime errors",
#                     "passed": True
#                 }]
#             }

#         for t in test_spec["tests"]:
#             call = t["call"]
#             expected = t["expected"]
#             description = t.get("description", "")

#             try:
#                 actual = eval(call, {}, local_env)
#                 passed = actual == expected
#             except Exception as e:
#                 actual = f"Exception: {str(e)}"
#                 passed = False

#             test_results.append({
#                 "test": call,
#                 "description": description,
#                 "expected": expected,
#                 "got": actual,
#                 "passed": passed
#             })

#             if not passed:
#                 return {
#                     "passed": False,
#                     "error": "One or more evaluation tests failed",
#                     "test_results": test_results
#                 }

#         return {
#             "passed": True,
#             "error": None,
#             "test_results": test_results
#         }

#     return evaluate


#------------------------------------------------------------------------new code feb


import json
import re
import traceback
from util.llm import get_llm


def evaluator_agent():
    """
    Hybrid execution-based evaluator.

    Priority order:
    1. Deterministic manual tests for known benchmark problems
    2. LLM-generated tests for unseen problems (fallback)
    """

    llm = get_llm(role="reviewer")

    # ---------------------------------------------------------
    # Utility: Safe JSON extraction from LLM output
    # ---------------------------------------------------------
    def safe_parse_json(text: str):
        text = text.strip()
        try:
            return json.loads(text)
        except Exception:
            pass

        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return None

        try:
            return json.loads(match.group())
        except Exception:
            return None

    # ---------------------------------------------------------
    # Utility: Check if a topological order is valid
    # ---------------------------------------------------------
    def is_valid_order(numTasks, deps, order):
        if not isinstance(order, list) or len(order) != numTasks:
            return False
        pos = {task: i for i, task in enumerate(order)}
        for dest, src in deps:
            if pos.get(src, -1) > pos.get(dest, -1):
                return False
        return True

    # ---------------------------------------------------------
    # Main evaluation function
    # ---------------------------------------------------------
    def evaluate(inputs):
        code = inputs["code"]
        problem = inputs["problem"].lower()

        local_env = {}
        test_results = []

        # -----------------------------------------------------
        # STEP 1: Execute generated code
        # -----------------------------------------------------
        try:
            exec(code, {}, local_env)
        except Exception:
            return {
                "passed": False,
                "error": "Generated code failed to execute",
                "traceback": traceback.format_exc(),
                "test_results": []
            }

        # =====================================================
        # MANUAL BENCHMARK: CLIMBING STAIRS
        # =====================================================
        if "climb" in problem and "stair" in problem:
            fn = None
            for name in ["climbStairs", "climb_stairs", "count_ways", "ways_to_climb"]:
                if name in local_env:
                    fn = local_env[name]
                    break

            if fn is None:
                return {
                    "passed": False,
                    "error": "No valid climbing stairs function found",
                    "test_results": []
                }

            tests = [
                (1, 1, "1 stair"),
                (2, 2, "2 stairs"),
                (3, 3, "3 stairs"),
                (5, 8, "5 stairs"),
            ]

            for n, expected, desc in tests:
                try:
                    result = fn(n)
                    passed = result == expected
                except Exception as e:
                    result = f"Exception: {e}"
                    passed = False

                test_results.append({
                    "test": f"{fn.__name__}({n})",
                    "description": desc,
                    "expected": expected,
                    "got": result,
                    "passed": passed
                })

                if not passed:
                    return {
                        "passed": False,
                        "error": "Manual test failed",
                        "test_results": test_results
                    }

            return {"passed": True, "error": None, "test_results": test_results}

        # =====================================================
        # MANUAL BENCHMARK: TASK DEPENDENCY / TOPO SORT
        # =====================================================
        if "task" in problem and "depend" in problem:
            fn = None
            for name in ["findOrder", "canFinish", "canFinishTasks"]:
                if name in local_env:
                    fn = local_env[name]
                    break

            if fn is None:
                return {
                    "passed": False,
                    "error": "No task dependency function found",
                    "test_results": []
                }

            tests = [
                ("Linear chain", (4, [[1, 0], [2, 1], [3, 2]]), [0, 1, 2, 3]),
                ("Cycle", (2, [[0, 1], [1, 0]]), []),
                ("Branching", (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), None),
                ("No deps", (3, []), [0, 1, 2]),
                ("Single", (1, []), [0]),
                ("Complex cycle", (4, [[0,1],[1,2],[2,3],[3,1]]), [])
            ]

            for desc, args, expected in tests:
                try:
                    result = fn(*args)
                    passed = (
                        is_valid_order(*args, result)
                        if expected is None
                        else result == expected
                    )
                except Exception as e:
                    result = f"Exception: {e}"
                    passed = False

                test_results.append({
                    "test": f"{fn.__name__}{args}",
                    "description": desc,
                    "expected": expected if expected else "Any valid order",
                    "got": result,
                    "passed": passed
                })

                if not passed:
                    return {
                        "passed": False,
                        "error": "Manual test failed",
                        "test_results": test_results
                    }

            return {"passed": True, "error": None, "test_results": test_results}

        # =====================================================
        # HYBRID FALLBACK: LLM-GENERATED TESTS
        # =====================================================
        try:
            prompt = f"""
You are a code evaluator.

Return ONLY valid JSON in this format:

{{
  "tests": [
    {{
      "call": "function_call_here",
      "expected": expected_value,
      "description": "what this test checks"
    }}
  ]
}}

Problem:
{inputs["problem"]}

Code:
{code}
"""
            response = llm.invoke(prompt)
            test_spec = safe_parse_json(response.content)
        except Exception:
            test_spec = None

        # -----------------------------------------------------
        # If LLM output is unusable → smoke pass
        # -----------------------------------------------------
        if not test_spec or "tests" not in test_spec:
            return {
                "passed": True,
                "error": None,
                "test_results": [{
                    "test": "Smoke test",
                    "description": "Code executed successfully",
                    "passed": True
                }]
            }

        valid_tests = 0

        for t in test_spec["tests"]:
            if not isinstance(t, dict):
                continue
            if "call" not in t or "expected" not in t:
                continue

            valid_tests += 1
            call = t["call"]
            expected = t["expected"]
            description = t.get("description", "")

            try:
                actual = eval(call, {}, local_env)
                passed = actual == expected
            except Exception as e:
                actual = f"Exception: {e}"
                passed = False

            test_results.append({
                "test": call,
                "description": description,
                "expected": expected,
                "got": actual,
                "passed": passed
            })

            if not passed:
                return {
                    "passed": False,
                    "error": "LLM-generated test failed",
                    "test_results": test_results
                }

        # No valid structured tests → smoke pass
        if valid_tests == 0:
            return {
                "passed": True,
                "error": None,
                "test_results": [{
                    "test": "Smoke test",
                    "description": "LLM returned no valid structured tests",
                    "passed": True
                }]
            }

        return {
            "passed": True,
            "error": None,
            "test_results": test_results
        }

    return evaluate
