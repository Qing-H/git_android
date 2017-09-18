import os
test_path = os.path.abspath("report.html")
print(test_path)
test_path2 = os.path.dirname(os.path.dirname(os.path.abspath("report.html")))
print(test_path2)