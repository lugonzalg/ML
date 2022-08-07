#!/bin/bash

if [[ "$1" = "run" ]]; then
	docker run -ti -v ${PWD}:/tmp pyenv
fi
