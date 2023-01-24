FROM httpd

COPY index.html /usr/local/apache2/htdocs/

COPY .htaccess /usr/local/apache2/htdocs/

COPY httpd.conf /usr/local/apache2/conf/
#RUN sed -i '286s/AllowOverride None/AllowOverride AuthConfig/' /usr/local/apache2/conf/httpd.conf

RUN echo "buddhi" | htpasswd -ic /etc/www.passwd buddhi

EXPOSE 80
#hello
