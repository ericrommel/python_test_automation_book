class BaseTest:
    def setup(self):
        print("Setting up the test")
        
    def run(self):
        print("Running the test....")
        
    def teardown(self):
        print("Test run has finished, clearing the created artefacts")

class LocalTest(BaseTest):        
    def __init__(self, os_name):
        self.name = os_name
        
    def setup(self):
        super().setup()
        print("Changing parameters for a LOCAL run")
        
    def run(self):
        super().run()
        print(f"Test is running now on a LOCAL machine with {self.name}")
        print("Report is added to log file for LOCAL run")
        
    def teardown(self):
        super().teardown()
        print("1 item was deleted from a local folder\n")
        
class AutoTest(BaseTest):    
    folder = "\reports"        
    def __init__(self, VM_name, report_folder):
        self.name = VM_name
        self.folder = report_folder
        
    def setup(self):
        super().setup()
        print("Environment is ready for an AUTO run")
        
    def run(self):
        super().run()
        print(f"Auto test is running now on a {self.name}")
        print(f"Report is added to {self.folder}")
        
    def teardown(self):
        super().teardown()
        print("Connection was closed\n")
        
test_case_01 = AutoTest("Linux Server", r"\reports\daily_run")
test_case_01.setup()
test_case_01.run()
test_case_01.teardown()

test_case_02 = AutoTest("Windows Server", r"\reports\05_12_2024")
test_case_02.setup()
test_case_02.run()
test_case_02.teardown()

# The child class inherits methods from the parent class
test = LocalTest("Win11")
test.setup() 
test.run() 
test.teardown()