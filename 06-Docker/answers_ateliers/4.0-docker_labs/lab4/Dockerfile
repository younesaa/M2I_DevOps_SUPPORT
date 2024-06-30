FROM centos:latest

# Update the base image and install Apache
RUN yum -y update \
    && yum -y install httpd \
    && yum clean all \
    && rm -rf /var/cache/yum

# Create a simple HTML file for the homepage
RUN echo "Welcome to Oracle - Docker Training Session Home Page created using Dockerfile" > /var/www/html/index.html

# Expose port 80 to allow HTTP traffic
EXPOSE 80

# Start Apache in the foreground
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]