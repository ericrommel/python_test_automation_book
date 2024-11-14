steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]  # Duplicate of steps_1

# Convert each scenario's steps to frozensets
scenario_1 = frozenset(steps_1)
scenario_2 = frozenset(steps_2)
scenario_3 = frozenset(steps_3)

# Dictionary of scenarios with frozensets
dic_scenarios = {
    "Test Case 1": scenario_1,
    "Test Case 2": scenario_2,
    "Test Case 3": scenario_3
}

# Function to check if a new test scenario already exists
def check_scenario(test_name, new_steps, existing_scenarios):
    steps_set = frozenset(new_steps)
    
    if steps_set in existing_scenarios.values():
        print(f"The scenario for '{test_name}' already exists.")
    else:
        # Add the new scenario to the dictionary
        existing_scenarios[test_name] = steps_set
        print(f"Scenario '{test_name}' added successfully.")


new_steps = ["open browser", "navigate to page", "click login"]  # Same steps as Test Case 1
check_scenario("Test Case 4", new_steps, dic_scenarios) # Output: Should indicate that it matches Test Case 1
unique_steps = ["open browser", "navigate to page", "close pop-up", "check header"]
check_scenario("Test Case 5", unique_steps, dic_scenarios)