# opencv-stitch

## 参考

https://qiita.com/niwasawa/items/03b1496dbb360ca157e0
https://github.com/sjitech/ubuntu-with-utils/blob/master/Dockerfile


```
[1755 ms] Start: Run: docker run --sig-proxy=false -a STDOUT -a STDERR --mount type=bind,source=c:\github\opencv-stitch,target=/workspaces/opencv-stitch,consistency=cached --mount type=volume,src=vscode,dst=/vscode -l vsch.local.folder=c:\github\opencv-stitch -l vsch.quality=stable -l vsch.remote.devPort=0 --entrypoint /bin/sh python-opencv -c echo Container started
docker: Error response from daemon: invalid mount config for type "bind": invali
d mount path: 'c:/github/opencv-stitch' mount path must be absolute.
See 'docker run --help'.
[2250 ms] Start: Run: docker ps -q -a --filter label=vsch.local.folder=c:\github\opencv-stitch --filter label=vsch.quality=stable
[2798 ms] Command failed: docker run --sig-proxy=false -a STDOUT -a STDERR --mount type=bind,source=c:\github\opencv-stitch,target=/workspaces/opencv-stitch,consistency=cached --mount type=volume,src=vscode,dst=/vscode -l vsch.local.folder=c:\github\opencv-stitch -l vsch.quality=stable -l vsch.remote.devPort=0 --entrypoint /bin/sh python-opencv -c echo Container started
trap "exit 0" 15

while sleep 1 & wait $!; do :; done
```