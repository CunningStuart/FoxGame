run:
	@python main.py

run_tests:
	@pytest -v

exe:
	@rm -rf dist
	pyinstaller main.py --noconsole
	# @xcopy "mdf2csv" "dist\TopconDiagnosticsViewer\mdf2csv" //h //i //c //k //e //r //y //q

clean:
	@rm -rf dist
	@rm -rf build
	@rm -rf main.spec

pep8:
	@autopep8 --in-place -a -a main.py

	@autopep8 --in-place -a -a src/FoxGame.py