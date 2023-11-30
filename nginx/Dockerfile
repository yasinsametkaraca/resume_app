FROM ngix:1.21-alpine

# remove the default configuration file.
RUN rm /etc/nginx/conf.d/default.conf

# copy the custom configuration file from the current directory and paste it inside the container's directory.
COPY nginx.conf /etc/nginx/conf.d




