# Use a lightweight web server image (nginx in this case)
FROM nginx:alpine

# Copy the HTML file into the nginx server directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Command to run nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
