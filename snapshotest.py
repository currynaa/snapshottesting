import boto3
def bytes_to_gb(bytes):
  gb = bytes / (1024 ** 3)
  return gb

#array=["snap-076884d5a67d396ef","snap-0963b3841d37bed99","snap-0c31ec0cdbd8336a8"]
array=["snap-0af649aba5ba65104"]

ebs = boto3.client('ebs',region_name="us-east-1")
for arr in array:
  #print(arr)
  response = ebs.list_snapshot_blocks(
  #SnapshotId="snap-0963b3841d37bed99"
  SnapshotId=arr
  )
  count=0

for res in response["Blocks"]:
  count=count+1
  #print(count)
  #print(res['BlockIndex'])
  sizeinbytes=count*524288
  #bytes_to_gb(sizeinbytes)
  print(arr + " " + str(bytes_to_gb(count*524288)))
