'''
Research about fronzenset(). You are building a test automation framework and want to store a collection of test case scenarios (with unique steps) in an immutable set so that the test scenarios can’t be altered. Each test scenario is a list of test steps, and you want to avoid duplicates.
Use frozenset() to store the test steps of each scenario in an immutable set.
Store each test scenario in a dictionary where the key is the test case name and the value is the frozenset of steps
Write a function that, given a test case name, prints whether the scenario already exists in the dictionary
Examples of test steps for different scenarios:
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login"] # duplicate steps
'''

test_scenarios = {}

def add_test_scenario(test_case_name, steps):
    steps_frozenset = frozenset(steps)
    if test_case_name not in test_scenarios:
        test_scenarios[test_case_name] = steps_frozenset
        print(f"Test scenario '{test_case_name}' added.")
    else:
        print(f"Test scenario '{test_case_name}' already exists.")


def check_test_scenario(test_case_name):
    if test_case_name in test_scenarios:
        print(f"Test scenario '{test_case_name}' exists.")
    else:
        print(f"Test scenario '{test_case_name}' does not exist.")


# already existing test steps
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]

# already existing tests scenarios
add_test_scenario("Login Test", steps_1)
add_test_scenario("Fill Form Test", steps_2)


while True:
    answer = input("lets test the code? (y/n): ")
    if answer == 'y':
        test_case_name = str(input("input test case name: "))
        check_test_scenario(test_case_name)
        print(test_scenarios)
    else:
        print(f"doh, you've stopped the verification")
        break




