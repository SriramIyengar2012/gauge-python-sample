From python
ARG gauge_version
ARG gauge_python_version
ARG gauge_html_report_version

ARG gauge_package=gauge-${gauge_version}-linux.x86_64.zip
ARG gauge_python_package=gauge-python-${gauge_python_version}.zip
ARG gauge_html_report_package=html-report-${gauge_html_report_version}-linux.x86_64.zip
RUN wget https://github.com/getgauge/gauge/releases/download/v${gauge_version}/${gauge_package}
RUN unzip ${gauge_package}
RUN mv gauge /usr/bin
RUN rm ${gauge_package}

RUN wget https://github.com/getgauge/gauge-python/releases/download/v${gauge_python_version}/${gauge_python_package}
RUN gauge install python --file ${gauge_python_package}

RUN wget https://github.com/getgauge/html-report/releases/download/v${gauge_html_report_version}/${gauge_html_report_package}
RUN gauge install html-report --file ${gauge_html_report_package}

RUN mkdir automation-test
COPY / automation-test/
WORKDIR "/automation-test"
CMD gauge run specs