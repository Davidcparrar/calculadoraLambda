FROM public.ecr.aws/lambda/python:3.12

# Copy function code
COPY calculator.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

RUN mkdir src
COPY src/ ${LAMBDA_TASK_ROOT}/src/
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)

CMD [ "calculator.lambda_handler" ]

