# Getting the base Image
# alternative : "FROM scratch" -> Empty base image
FROM ubuntu:latest
# Label (earlier called Maintainer) -optional to keep track of author
LABEL pranjalbiyani <pranjalbiyani1996@gmail.com>
# Executing intial set of commands after the ubuntu image is built
# RUN commands get executed upon creation of the image,
# CMD commands get executed after running images as containers
RUN apt-get update && apt-get install -y python3-pip 
RUN apt-get install -y python3
# For linux ,package manager would be "apt" - in place of apk
CMD ["python3","--version"]

# docker images - to check images presently built
# docker build -t Imagename:versionname .