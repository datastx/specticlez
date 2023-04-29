ANTLR_IMAGE_NAME = my-antlr4-image
ANTLR_VER=4.12.0

antlr-build:
	docker build -t $(ANTLR_IMAGE_NAME) --build-arg ANTLR_VERSIO=$(ANTLR_VER) -f Dockerfiles/antlr4.dockerfile .

antlr-compile: antlr-build
	docker run --rm -it -v $(shell pwd)/app:/app $(ANTLR_IMAGE_NAME) /bin/bash -c "cd /app/grammars && java -jar /antlr-$(ANTLR_VER)-complete.jar -Dlanguage=Python3 LookMLLexer.g4 -o . && java -jar /antlr-$(ANTLR_VER)-complete.jar -Dlanguage=Python3 LookMLParser.g4 -o ."

run: antlr-compile
	(. .venv/bin/activate && export PYTHONPATH="$(PYTHONPATH):/Users/brianmoore/githib.com/datastx/specticlez/app" && python3 app/main.py)
