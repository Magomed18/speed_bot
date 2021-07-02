import speedtest
from hurry.filesize import size

test = speedtest.Speedtest()

#Getting servers
print('Loading server list...')
a = test.get_best_server()
print(a['host'], a['name'], a['country'])

#Getting upload and download speed
download_result = test.download() / 1024 / 1024
upload_result = test.upload() / 1024 / 1024

print( "%.2f" % download_result)
print("%.2f" % upload_result)


