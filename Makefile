all:
	swagger_py_codegen -s  api.yaml -p commvault_app --ui --spec . 
	pip install -r requirements.txt
