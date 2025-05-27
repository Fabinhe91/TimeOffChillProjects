# Step 1: Use Nginx as a base image
FROM nginx:alpine

# Step 2: Copy the HTML file into the Nginx container
COPY index.html /usr/share/nginx/html/

# Step 3: Expose port 80 (default for Nginx)
EXPOSE 80

# Step 4: Start Nginx
CMD ["nginx", "-g", "daemon off;"]
