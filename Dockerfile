FROM python

ADD ./robot-devil.py /root/app/robot-devil.py
ADD ./yarnSpin/fanFicMadLib.py /root/app/yarnSpin/fanFicMadLib.py
ADD ./yarnSpin/__init__.py /root/app/yarnSpin/__init__.py
ADD ./deploy/install_deps.py /root/app/install_deps.py

RUN pip install discord
RUN pip install numpy
RUN pip install nltk
RUN pip install beautifulsoup4
RUN pip install requests

RUN python /root/app/install_deps.py

CMD python /root/app/robot-devil.py $BOT_TOKEN
