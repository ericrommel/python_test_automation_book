# List of steps:
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"]  # duplicate steps

# Use frozenset() to store the test steps of each scenario in an immutable set:
scenario_1 = frozenset(steps_1)
scenario_2 = frozenset(steps_2)
scenario_3 = frozenset(steps_3)

# Store each test scenario in a dictionary where the key is the test case name and the value is the frozenset of steps:
dic_scenarios = {"Test Case 1": scenario_1, "Test Case 2": scenario_2, "Test Case 3": scenario_3, }
print(type(dic_scenarios))

new_steps = ["open browser", "navigate to page", "click login"]


# new_steps = "open browser", "navigate to page", "fill form"


# Write a function that, given a test case name, prints whether the scenario already exists in the dictionary
def ifStepsExist(key, dictionary, new_steps):
    new_scenario = frozenset(new_steps)
    new_list = []
    for test_case_name, steps in dictionary.items():
        if new_scenario == steps:
            new_list.append(test_case_name)
    if new_list:
        print(f"{key} has the same steps as: {new_list}")
    else:
        print("No such steps in the dictionary.")
    return new_list


ifStepsExist("Test Case 4", dic_scenarios, new_steps)
