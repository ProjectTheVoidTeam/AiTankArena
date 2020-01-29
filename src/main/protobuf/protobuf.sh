protoc -I=./ --java_out=../java/ --python_out=../python/ ./*.proto
cp ./*.proto ../javascript/protobuf