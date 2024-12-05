class TestClass():    
    def __init__(self, name):
        self.name = name
    
    def setup(self):
        print("Connection to DB is established")
        print("SQL query is executed")
        
    def run(self):
        print(f"Test case {self.name} is running....")
        print("Run is finished")
        
    def teardown(self):
        print("Connection is closed")
        print("Report is generated")
        
dbtest = TestClass("Test01")
dbtest.setup()
dbtest.run()
dbtest.teardown()