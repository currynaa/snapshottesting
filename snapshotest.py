1 import boto3
  2
  3 def bytes_to_gb(bytes):
  4     gb = bytes / (1024 ** 3)
  5     return gb
  6
  7 #array=["snap-076884d5a67d396ef","snap-0963b3841d37bed99","snap-0c31ec0cdbd8336a8"]
  8 array=["snap-0af649aba5ba65104"]
  9
 10 ebs = boto3.client('ebs',region_name="us-east-1")
 11 for arr in array:
 12     #print(arr)
 13     response = ebs.list_snapshot_blocks(
 14             #SnapshotId="snap-0963b3841d37bed99"
 15             SnapshotId=arr
 16         )
 17
 18     count=0
 19
 20     for res in response["Blocks"]:
 21         count=count+1
 22     #print(count)
 23     #print(res['BlockIndex'])
 24     sizeinbytes=count*524288
 25     #bytes_to_gb(sizeinbytes)
 26     print(arr + " " + str(bytes_to_gb(count*524288)))
