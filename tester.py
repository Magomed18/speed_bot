import speedtest
from hurry.filesize import size

test = speedtest.Speedtest()

#Getting upload and download speed
download_result = test.download() / 1024 / 1024
upload_result = test.upload() / 1024 / 1024


