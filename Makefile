PROJECT_NAME := test-compliance/cuphd-health-status-service

export PROJECT_NAME := ${PROJECT_NAME}

.PHONY: build docker-deploy-dev docker-deploy-test docker-deploy-prod

build: Dockerfile
	docker build -f Dockerfile -t ${PROJECT_NAME}:latest .

deploy-dev: build
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 779619664536.dkr.ecr.us-east-2.amazonaws.com
	docker tag ${PROJECT_NAME}:latest 779619664536.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:dev
	docker push 779619664536.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:dev

deploy-test: build
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 225486102836.dkr.ecr.us-east-2.amazonaws.com
	docker tag ${PROJECT_NAME}:latest 225486102836.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:test
	docker push 225486102836.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:test

deploy-prod: build
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 225486102836.dkr.ecr.us-east-2.amazonaws.com
	docker tag 225486102836.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:test 225486102836.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:prod
	docker push 225486102836.dkr.ecr.us-east-2.amazonaws.com/${PROJECT_NAME}:prod

up: build
	docker-compose up

down:
	docker-compose down

