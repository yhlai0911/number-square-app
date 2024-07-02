# 使用官方 Python 運行時作為父映像
FROM python:3.9

# 設置工作目錄
WORKDIR /app

# 將當前目錄內容複製到容器中的 /app
COPY . /app

# 安裝必要的包
RUN pip install fastapi uvicorn

# 暴露端口 8000 供外部訪問
EXPOSE 8000

# 運行應用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]