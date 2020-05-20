FROM ocrd/tesserocr

COPY sources.list /etc/apt/sources.list

RUN mkdir /root/.pip

COPY pip.conf /root/.pip/pip.conf

RUN apt-get update \
  && apt-get install -y gcc build-essential tesseract-ocr libxtst6 libglib2.0-0 libsm6 libfontconfig1 libxrender1 
  
RUN pip3 install tensorflow==1.14.0 opencv-python pytesseract request gunicorn gevent

ENV TESSDATA_PREFIX /usr/share/tesseract-ocr/4.00/tessdata

COPY traineddata/chi_sim.traineddata /usr/share/tesseract-ocr/4.00/tessdata/chi_sim.traineddata

COPY traineddata/chi_sim_vert.traineddata /usr/share/tesseract-ocr/4.00/tessdata/chi_sim_vert.traineddata

COPY ./data /data

WORKDIR /data

ENTRYPOINT ["/bin/bash","./run.sh"]

EXPOSE 5000
