ANTLR_IMAGE_NAME = my-antlr4-image
ANTLR_VER=4.12.0
CURRENT_DIR=$(shell pwd)
FILE_DROP=../engine/antlr/

antlr-build:
	docker build -t $(ANTLR_IMAGE_NAME) --build-arg ANTLR_VERSION=$(ANTLR_VER) -f Dockerfiles/antlr4.dockerfile .

antlr-compile: antlr-build
	docker run --rm -it -v $(CURRENT_DIR)/app:/app $(ANTLR_IMAGE_NAME) /bin/bash -c "cd /app/grammars && java -jar /antlr-$(ANTLR_VER)-complete.jar -Dlanguage=Python3 LookMLLexer.g4 -o $(FILE_DROP) && java -jar /antlr-$(ANTLR_VER)-complete.jar -Dlanguage=Python3 LookMLParser.g4 -o $(FILE_DROP)"

run: antlr-compile
	# (. .venv/bin/activate && export PYTHONPATH="$(PYTHONPATH):$(CURRENT_DIR)/app" && python3 $(CURRENT_DIR)/app/main.py)

cli:
	(. .venv/bin/activate && export PYTHONPATH="$(PYTHONPATH):$(CURRENT_DIR)/app" && python3 $(CURRENT_DIR)/app/main.py -f test.txt -c here -l json)

test:
	(. .venv/bin/activate && export PYTHONPATH="$(PYTHONPATH):$(CURRENT_DIR)/app" && python3 -m unittest test/app/engine/test_tree.py)