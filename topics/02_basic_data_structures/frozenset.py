"""Research about fronzenset(). You are building a test automation framework and want to store a collection of test case scenarios (with unique steps)
 in an immutable set so that the test scenarios can’t be altered.
  Each test scenario is a list of test steps, and you want to avoid duplicates.
Use frozenset() to store the test steps of each scenario in an immutable set.
Store each test scenario in a dictionary where the key is the test case name and the value is the frozenset of steps
Write a function that, given a test case name, prints whether the scenario already exists in the dictionary
Examples of test steps for different scenarios:
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"] # duplicate steps"""

# Function to check if a new test scenario already exists
def check_scenario(test_name, new_steps, existing_scenarios):
    duplicates = []
    for key, value in existing_scenarios.items():
        if value == frozenset(new_steps):
            duplicates.append(key)
    return duplicates

# Example usage
dic_scenarios = {
    "Test Case 1": frozenset(["open browser", "navigate to page", "click login"]),
    "Test Case 2": frozenset(["open browser", "navigate to page", "fill form"]),
    "Test Case 3": frozenset(["open browser", "navigate to page", "click login"])
}

new_steps = ["open browser", "navigate to page", "click login"]  # Same steps as Test Case 1
result = check_scenario("Test Case 4", new_steps, dic_scenarios) # Output: Should indicate that it matches Test Case 1
print(result) #['Test Case 1', 'Test Case 3']