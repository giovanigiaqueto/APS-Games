
uninstall:
	python3 -m pip uninstall APS-Games

install:
	python3 -m pip install dist/*.whl

build:
	python3 setup.py bdist_wheel

refresh: build uninstall install
