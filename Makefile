all:
	pip install -r requirements.txt
	swagger_py_codegen -s api.yaml -p commvault_app --ui . 
