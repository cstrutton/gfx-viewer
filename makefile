.DEFAULT_GOAL := help

.PHONY: clean run exec help

image-name = gfx-viewer
container-name = gfx-viewer
port = 6481

clean: ## Stop and remove the app container
	docker stop $(container-name)
	docker rm $(container-name)
	
run:  ## Build and run the app
	docker build -t $(image-name) .
	docker run -d --name $(container-name) -p $(port):80 $(image-name)

exec:  ## Start a bash shell in the container
	docker exec -ti $(container-name) /bin/bash

help: ## This help dialog.
	@echo "Welcome to the Gauge Viewer app\n"
    @IFS=$$'\n' ; \
    help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//'`); \
    for help_line in $${help_lines[@]}; do \
        IFS=$$'#' ; \
        help_split=($$help_line) ; \
        help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
        help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
        printf "%-30s %s\n" $$help_command $$help_info ; \
    done
