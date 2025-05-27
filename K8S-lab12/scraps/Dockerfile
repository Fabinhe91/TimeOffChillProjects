# Frontend Dockerfile (HTML or React App)
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port for frontend
EXPOSE 80

# Run the app
CMD ["npm", "start"]
