ANTLR_IMAGE_NAME = my-antlr4-image
ANTLR_VER=4.12.0
CURRENT_DIR=$(shell pwd)
FILE_DROP=../engine/antlr/

# Include the venv Makefile
include Makefile.venv

.PHONY: antlr-build
antlr-build:
	docker build -t $(ANTLR_IMAGE_NAME) --build-arg ANTLR_VERSION=$(ANTLR_VER) -f Dockerfiles/antlr4.dockerfile .

.PHONY: antlr-compile
antlr-compile: antlr-build
	docker run --rm -it -v $(CURRENT_DIR)/app:/app $(ANTLR_IMAGE_NAME) /bin/bash -c "cd /app/grammars && java -jar /antlr-$(ANTLR_VER)-complete.jar -Dlanguage=Python3 LookMLLexer.g4 -o $(FILE_DROP) && java -jar /antlr-$(ANTLR_VER)-complete.jar -Dlanguage=Python3 LookMLParser.g4 -o $(FILE_DROP)"

.PHONY: run
run: antlr-compile venv
	env PYTHONPATH="$(PYTHONPATH):$(CURRENT_DIR)/app" $(VENV)/python $(CURRENT_DIR)/app/main.py

.PHONY: cli
cli: venv
	env PYTHONPATH="$(PYTHONPATH):$(CURRENT_DIR)/app" $(VENV)/python $(CURRENT_DIR)/app/main.py -f test.txt -c here -l json

test: venv antlr-compile
	export PYTHONPATH=$(CURRENT_DIR)/app:$$PYTHONPATH; $(VENV)/pytest -v --tb=long


# New target to rebuild the virtual environment
.PHONY: rebuild-venv
rebuild-venv: clean-venv venv

# New target to open Python REPL with the correct PYTHONPATH
.PHONY: repl
repl: venv
	env PYTHONPATH="$(PYTHONPATH):$(CURRENT_DIR)/app" $(VENV)/python
