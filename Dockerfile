FROM node:10-alpine as frontend
WORKDIR /app
COPY frontend .
RUN npm install
RUN npm run build

FROM python:3.7-alpine
WORKDIR /app
COPY backend .
COPY --from=frontend /app/dist /vuedocker
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]