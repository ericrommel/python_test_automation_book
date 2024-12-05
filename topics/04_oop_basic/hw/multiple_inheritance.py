class BaseClass:
    def log(self, message):
        print(f"[Basic Log]: {message}")
        
class SetUpManager(BaseClass):
    def setup(self):
        self.log("Environment is ready")
        
class TestExecutor(BaseClass):
    def run_test(self, test_name):
        self.log(f"Running test: '{test_name}'")
        print(f"Test {test_name} executed.")
        
class ReportGenerator(BaseClass):
    def generate_report(self, test_name, result):
        self.log(f"Report is generated for '{test_name}'")
        print(f"Report result for '{test_name}' is {result}")
        
class SuperTestCase(SetUpManager, TestExecutor, ReportGenerator):
    def do_everything(self, test_name):
        self.setup()
        self.run_test(test_name)
        if("Test_should_pass" in test_name):
            result = "PASSED"
        else:
            result = "FAIL" 
        self.generate_report(test_name, result)
        print("---Test Completed---\n")
        
test_case = SuperTestCase()
test_case.do_everything("Test_should_pass")
print(SuperTestCase.mro())