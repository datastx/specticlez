ANTLR_IMAGE_NAME = my-antlr4-image

antlr-build:
	docker build -t $(ANTLR_IMAGE_NAME) -f Dockerfiles/antlr4.dockerfile .

antlr-compile: antlr-build
	docker run --rm -it -v $(shell pwd)/app:/app $(ANTLR_IMAGE_NAME) /bin/bash -c "cd /app/grammars && java -jar /antlr-4.12.0-complete.jar -Dlanguage=Python3 LookMLLexer.g4 -o . && java -jar /antlr-4.12.0-complete.jar -Dlanguage=Python3 LookMLParser.g4 -o ."

run: antlr-compile
	(. .venv/bin/activate && export PYTHONPATH="$(PYTHONPATH):/Users/brianmoore/githib.com/datastx/specticlez/app" && python3 app/main.py)
